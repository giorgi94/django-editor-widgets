# Django-editor-widgets


This package provides some custom widgets to use monaco or tinymce editors in django admin.

**remark**: From version 3.0 fields and extra widgets are removed to make code more flexible. Version with custom fields is in *v_2.0* branch.


## Installation

To install the package by `pip` run following command

```sh
# From Github (latest updates)
$ pip install git+https://github.com/giorgi94/django-editor-widgets.git
# Or
$ pip install django-editor-widgets
```

## Usage

To start using the package in your project, you need to open `settings.py` file and add following lines

```python
# settings.py
import os

# sets paths to static files for widgets
from djangoeditorwidgets.config import *


# Application definition

INSTALLED_APPS = [
    ...
    'djangoeditorwidgets',
    ...
]

```

### TinyMCE

To use tinymce editor in admin, we need to change default widget in the form with `TinymceWidget`


```python
# forms.py
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
```

### Monaco Editor

From version 3.0 is removed custom fields and extra widgets. To use monaco editor, we need to import `MonacoEditorWidget` and customize it

```python
# models.py
import json
from django.db import models

class JSONModel(models.Model):
    title = models.CharField(max_length=50)
    _text = models.TextField()

    @property
    def text(self):
        return json.laods(self._text)

    @text.setter
    def text(self, val):
        self._text = json.dumps(val, ensure_ascii=False)

    def __str__(self):
        return self.title

# forms.py
from django import forms
from djangoeditorwidgets.widgets import MonacoEditorWidget
from .models import JSONModel


class JsonModelForm(forms.ModelForm):
    class Meta:
        model = JSONModel
        fields = "__all__"
        widgets = {
            "_text": MonacoEditorWidget(
                attrs={"data-wordwrap": "on", "data-language": "json"}
            )
        }
```

## Remark

Unlike other django package which are for Rich web editors, this package allows developer to fully use capablities and custom plugins for the web editor, like tinymce or monaco, since configurations doesn't go through django settings.