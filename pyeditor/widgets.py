import os
import json
from xml.etree import ElementTree as xmltree

from django import forms
from django.conf import settings
from django.utils import translation as trans
from django.contrib.admin.widgets import AdminTextareaWidget
from django.utils.translation import ugettext_lazy as _


class XMLWidget(AdminTextareaWidget):

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        attrs = context['widget']['attrs']
        attrs.update({
            'monaco-editor': 'true',
            'data-language': 'xml',
            'data-wordwrap': 'off',
            'data-minimap': 'false'
        })
        return context

    def format_value(self, value):
        if value is None:
            return ""
        if type(value) == str:
            return value
        return xmltree.tostring(value, encoding='utf8', method='xml').decode()

    class Media:
        js = settings.MONACO_EDITOR_STATIC['js']
        css = settings.MONACO_EDITOR_STATIC['css']


class JSONWidget(AdminTextareaWidget):

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        attrs = context['widget']['attrs']
        attrs.update({
            'monaco-editor': 'true',
            'data-language': 'json',
            'data-wordwrap': 'off',
            'data-minimap': 'false'
        })
        return context

    def format_value(self, value):
        if value is None:
            return "{}"
        if type(value) == str:
            return value
        return json.dumps(value, indent=4, ensure_ascii=False, sort_keys=True)

    class Media:
        js = settings.MONACO_EDITOR_STATIC['js']
        css = settings.MONACO_EDITOR_STATIC['css']


class TinymceWidget(forms.Textarea):

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        attrs = context['widget']['attrs']
        attrs.update({
            'tinymce-editor': True,
        })
        return context

    class Media:
        js = settings.TINYMCE_EDITOR_STATIC['js']
        css = settings.TINYMCE_EDITOR_STATIC['css']


class MonacoEditorWidget(forms.Textarea):

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        attrs = {
            'monaco-editor': 'true',
            'data-language': 'html',
            'data-wordwrap': 'off',
            'data-minimap': 'false'
        }
        attrs.update(context['widget']['attrs'])
        context['widget']['attrs'] = attrs
        return context

    class Media:
        js = (
            '/static/monaco/loader.js',
            '/static/monaco/monaco.config.js',
        )
        css = {
            'screen': ("/static/monaco/monaco.custom.css", )
        }
