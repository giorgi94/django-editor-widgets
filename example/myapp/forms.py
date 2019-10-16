from django import forms
from djangoeditorwidgets.widgets import TinymceWidget, MonacoEditorWidget
from .models import TextModel, XMLModel, JSONModel


class TextModelForm(forms.ModelForm):
    class Meta:
        model = TextModel
        fields = "__all__"
        widgets = {"text": TinymceWidget()}


class JsonModelForm(forms.ModelForm):
    class Meta:
        model = JSONModel
        fields = "__all__"
        widgets = {
            "_text": MonacoEditorWidget(
                attrs={"data-wordwrap": "on", "data-language": "json"}
            )
        }


class XmlModelForm(forms.ModelForm):
    class Meta:
        model = XMLModel
        fields = "__all__"
        widgets = {
            "_text": MonacoEditorWidget(
                attrs={"data-wordwrap": "on", "data-language": "xml"}
            )
        }
