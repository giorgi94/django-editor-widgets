from django.db import models

import json
from xml.etree import ElementTree as xmltree


class TextModel(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self):
        return self.title


class XMLModel(models.Model):
    title = models.CharField(max_length=50)
    _text = models.TextField()

    @property
    def text(self):
        return xmltree.fromstring(self._text)

    def __str__(self):
        return self.title


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
