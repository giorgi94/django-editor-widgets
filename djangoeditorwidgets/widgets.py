import json

from django import forms
from django.conf import settings


class TinymceWidget(forms.Textarea):
    def __init__(self, name="default", attrs={}):

        default_attrs = {
            "data-tinymce": name,
        }

        default_attrs.update(attrs)

        super().__init__(default_attrs)

    @property
    def media(self):

        config = settings.WEB_EDITOR_CONFIG["tinymce"]

        return forms.Media(js=config["js"], css=config["css"])


class MonacoEditorWidget(forms.Textarea):
    def __init__(
        self, name="default", language="html", wordwrap=True, minimap=False, attrs={}
    ):

        default_attrs = {
            "data-monaco": name,
            "data-language": language,
            "data-wordwrap": "on" if wordwrap else "off",
            "data-minimap": "on" if minimap else "off",
        }

        default_attrs.update(attrs)

        super().__init__(default_attrs)

    @property
    def media(self):

        config = settings.WEB_EDITOR_CONFIG["monaco"]

        return forms.Media(js=config["js"], css=config["css"])
