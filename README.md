# Django-editor-widgets


This package provides some custom widgets to use monaco or tinymce editors in django admin.


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

Now we can start using the widgets. To use tinymce we need to change widget in form
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

The package also provides custom field, and widget are already set for them.

```python
# models.py
from django.db import models
from djangoeditorwidgets.fields import XMLField



class XMLModel(models.Model):
    title = models.CharField(max_length=50)
    text = XMLField()

    def __str__(self):
        return self.title

```
