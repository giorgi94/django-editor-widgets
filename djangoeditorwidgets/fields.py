import json
from xml.etree import ElementTree as xmltree

from django import forms
from django.core import exceptions
from django.db.models import TextField
from django.utils.translation import ugettext_lazy as _

from .widgets import XMLWidget, JSONWidget


class JsonField(TextField):
    description = "JSON Field"

    def from_db_value(self, value, expression, connection):
        try:
            if value is None:
                return {}
            if type(value) == str:
                value = json.loads(value)
            return value
        except Exception as ex:
            return {}

    def to_python(self, value):
        try:
            if value is None:
                return {}
            if type(value) == str:
                value = json.loads(value)
            return value
        except Exception as ex:
            return {}

    def get_prep_value(self, value):
        try:
            if value is None:
                return "{}"
            if type(value) == str:
                return value
            return json.dumps(value, ensure_ascii=False)
        except Exception as e:
            return "{}"

    def _get_val_from_obj(self, value):
        return self.get_prep_value(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_prep_value(value)

    def clean(self, value, model_instance):
        try:
            value = super().clean(value, model_instance)
            if type(value) == str:
                return json.loads(value)
            return value
        except Exception:
            raise forms.ValidationError(_('JSON syntax error'))

    def formfield(self, **kwargs):
        widget = kwargs.get('widget')
        kwargs['widget'] = JSONWidget
        return super().formfield(**kwargs)


class XMLField(TextField):
    description = "XML Field"

    @staticmethod
    def normalize(value):
        if type(value) == str:
            return xmltree.fromstring(value)
        return value

    def from_db_value(self, value, expression, connection):
        try:
            if value is None:
                return None
            return xmltree.fromstring(value)
        except Exception as e:
            return None

    def get_prep_value(self, value):
        try:
            if type(value) == str:
                return value
            return xmltree.tostring(
                value, encoding='utf8', method='xml').decode()
        except Exception as e:
            return ""

    def _get_val_from_obj(self, value):
        return self.get_prep_value(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_prep_value(value)

    def clean(self, value, model_instance):
        try:
            value = super().clean(value, model_instance)
            if type(value) == str:
                return xmltree.fromstring(value)
            return value
        except Exception as e:
            raise forms.ValidationError(_('XML syntax error'))

    def formfield(self, **kwargs):
        kwargs['widget'] = XMLWidget
        return super().formfield(**kwargs)
