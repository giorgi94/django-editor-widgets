# Django-editor-widgets


This package provides some custom widgets to use monaco or tinymce editors in django admin.


## Installation

To install the package by `pip` run following command

```sh
$ pip install git+https://github.com/giorgi94/django-editor-widgets.git
```

## Usage

To start using the package in your project, you need to open `settings.py` file and add following lines

```python
# settings.py
import os

# sets paths to static files for widgets
from djangoeditorwidgets.defaults import *


# Application definition

INSTALLED_APPS = [
    ...
    'djangoeditorwidgets',
    ...
]

```

Now we can start using the widgets. To use tinymce we need to override widget in form
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

The package also provides custom fields, and widgets are already set for them.

```python
# models.py
from django.db import models
from djangoeditorwidgets.fields import XMLField, JsonField


class TextModel(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self):
        return self.title


class XMLModel(models.Model):
    title = models.CharField(max_length=50)
    text = XMLField()

    def __str__(self):
        return self.title


class JSONModel(models.Model):
    title = models.CharField(max_length=50)
    text = JsonField()

    def __str__(self):
        return self.title

```
You don't need to use this fields and only change widgets in forms, but this fields provide simple validations.