import os
import json
from xml.etree import ElementTree as xmltree

from django import forms
from django.conf import settings
from django.utils import translation as trans
from django.contrib.admin.widgets import AdminTextareaWidget
from django.utils.translation import ugettext_lazy as _


class TinymceWidget(forms.Textarea):

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        attrs = context['widget']['attrs']
        attrs.update({
            'tinymce-editor': True,
        })
        return context

    class Media:
        staticfiles = settings.WEB_EDITOR_STATICFILES['tinymce']
        js = staticfiles['js']
        css = staticfiles['css']


class MonacoEditorWidget(forms.Textarea):

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        attrs = {
            'monaco-editor': 'true',
            'data-language': 'html',
            'data-wordwrap': 'off',
            'data-minimap': 'false'
        }
        attrs.update(context['widget']['attrs'])
        context['widget']['attrs'] = attrs
        return context

    class Media:
        staticfiles = settings.WEB_EDITOR_STATICFILES['monaco']
        js = staticfiles['js']
        css = staticfiles['css']
