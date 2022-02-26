from django import forms
from djangoeditorwidgets.widgets import TinymceWidget, MonacoEditorWidget
from .models import TextModel, XMLModel, JSONModel


class TextModelForm(forms.ModelForm):
    class Meta:
        model = TextModel
        fields = "__all__"
        widgets = {"text": TinymceWidget(name="default")}


class JsonModelForm(forms.ModelForm):
    class Meta:
        model = JSONModel
        fields = "__all__"
        widgets = {
            "_text": MonacoEditorWidget(name="default", language="json", wordwrap=True)
        }


class XmlModelForm(forms.ModelForm):
    class Meta:
        model = XMLModel
        fields = "__all__"
        widgets = {
            "_text": MonacoEditorWidget(name="default", language="xml", wordwrap=True)
        }
