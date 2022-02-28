# Django-editor-widgets


This package provides some custom widgets to use monaco or tinymce editors in django admin.

**remark**: From version 4.0 static files for tinymce and monaco editors are removed.


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
from pathlib import Path

# import configurations for editor
from djangoeditorwidgets.config import init_web_editor_config

# set base dir by Path instead of os.path
BASE_DIR = Path(__file__).resolve().parent.parent

# Application definition

INSTALLED_APPS = [
    ...
    'djangoeditorwidgets',
    ...
]


MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"

WEB_EDITOR_DOWNLOAD, WEB_EDITOR_CONFIG = init_web_editor_config(
    # set the directory where files are downloaded
    BASE_DIR / "static_cdn",
    # set static url prefix
    STATIC_URL
)


```

In current version uses `Path` instead of `os.path` to manage files and directories. If needed configuration parameters can be written manually

```python
from os.path import join

WEB_EDITOR_DOWNLOAD = {
    "to": BASE_DIR / "static_cdn",
    "tinymce": {
        "url": "https://download.tiny.cloud/tinymce/community/tinymce_5.10.3.zip",
        "target": "tinymce/js/tinymce",
    },
    "monaco": {
        "url": "https://registry.npmjs.org/monaco-editor/-/monaco-editor-0.32.1.tgz",
        "target": "package/min",
    },
}

WEB_EDITOR_CONFIG = {
    "tinymce": {
        "js": [
            join(STATIC_URL, "tinymce/tinymce.min.js"),
            join(STATIC_URL, "djangoeditorwidgets/tinymce/tinymce.config.js"),
            join(STATIC_URL, "djangoeditorwidgets/tinymce/tinymce.init.js"),
        ],
        "css": {
            "all": [
                join(STATIC_URL, "djangoeditorwidgets/tinymce/tinymce.custom.css"),
            ]
        },
    },
    "monaco": {
        "js": [
            join(STATIC_URL, "monaco/vs/loader.js"),
            join(STATIC_URL, "djangoeditorwidgets/monaco/monaco.config.js"),
        ],
        "css": {
            "all": [
                join(STATIC_URL, "djangoeditorwidgets/monaco/monaco.custom.css"),
            ]
        },
    },
}
```


### Commands

Static files are removed from the package, instead it provides management command to download and extract files to given  location

```bash
$ python manage.py download_editpr_scripts
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
            'text': TinymceWidget(name="default")
        }
```

By `name` argument we can modify selector and can define multiple configs for tinymce editor.


### Monaco Editor

In lastest verions of `sqlite3` and `mariadb` we now have `json field`, it is more limited compared to `postgresql` but can handle json validation and parsing

```python
# models.py
import json
from django.db import models

class JSONModel(models.Model):
    title = models.CharField(max_length=50)
    text = models.JSONField(null=True)

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
            "text": MonacoEditorWidget(name="default", language="json", wordwrap=True)
        }

```

## Remark

Unlike other django package which are for Rich web editors, this package allows developer to fully use capablities and custom plugins for the web editor, like tinymce or monaco, since configurations doesn't go through django settings.