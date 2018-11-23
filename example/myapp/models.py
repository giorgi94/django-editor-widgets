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
