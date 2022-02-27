from django.db import models


class TextModel(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(null=True)

    def __str__(self):
        return self.title


class HTMLModel(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(null=True)

    def __str__(self):
        return self.title


class JSONModel(models.Model):
    title = models.CharField(max_length=50)
    text = models.JSONField(null=True)

    def __str__(self):
        return self.title
