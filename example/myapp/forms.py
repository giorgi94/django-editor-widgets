from django import forms
from djangoeditorwidgets.widgets import TinymceWidget, JSONWidget
from .models import TextModel


class TextModelForm(forms.ModelForm):

    class Meta:
        model = TextModel
        fields = '__all__'
        widgets = {
            'text': TinymceWidget()
        }


class JsonModelForm(forms.ModelForm):

    class Meta:
        model = TextModel
        fields = '__all__'
        widgets = {
            'text': JSONWidget()
        }
