from django import forms
from djangoeditorwidgets.widgets import TinymceWidget, MonacoEditorWidget
from .models import TextModel, HTMLModel, JSONModel


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
            "text": MonacoEditorWidget(name="default", language="json", wordwrap=True)
        }


class HTMLModelForm(forms.ModelForm):
    class Meta:
        model = HTMLModel
        fields = "__all__"
        widgets = {
            "text": MonacoEditorWidget(name="default", language="html", wordwrap=True)
        }
