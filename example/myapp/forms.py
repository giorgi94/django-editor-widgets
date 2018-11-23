from django import forms
from djangoeditorwidgets.widgets import TinymceWidget
from .models import TextModel


class TextModelForm(forms.ModelForm):

    class Meta:
        model = TextModel
        fields = '__all__'
        widgets = {
            'text': TinymceWidget()
        }
