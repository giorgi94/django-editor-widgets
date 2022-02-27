from django.contrib import admin

from .models import TextModel, HTMLModel, JSONModel

from .forms import TextModelForm, JsonModelForm, HTMLModelForm


@admin.register(TextModel)
class TextModelAdmin(admin.ModelAdmin):
    form = TextModelForm


@admin.register(HTMLModel)
class HTMLModelAdmin(admin.ModelAdmin):
    form = HTMLModelForm


@admin.register(JSONModel)
class JSONModelAdmin(admin.ModelAdmin):
    form = JsonModelForm
