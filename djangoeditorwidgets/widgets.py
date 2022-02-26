from django import forms
from django.conf import settings


class TinymceWidget(forms.Textarea):
    def __init__(self, name="default", attrs={}):
        super().__init__(attrs)

        self.name = name

    def get_context(self, name, value, attrs):
        context = super().get_context(
            name,
            value,
            {
                "data-tinymce": self.name,
                **attrs,
            },
        )
        return context

    @property
    def media(self):

        config = settings.WEB_EDITOR_CONFIG["tinymce"]

        return forms.Media(js=config["js"], css=config["css"])


class MonacoEditorWidget(forms.Textarea):
    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        attrs = {
            "monaco-editor": "true",
            "data-language": "html",
            "data-wordwrap": "off",
            "data-minimap": "false",
        }
        attrs.update(context["widget"]["attrs"])
        context["widget"]["attrs"] = attrs
        return context

    # class Media:
    #     staticfiles = settings.WEB_EDITOR_STATICFILES['monaco']
    #     js = staticfiles['js']
    #     css = staticfiles['css']
