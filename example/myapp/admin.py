from django.contrib import admin

from .models import TextModel, XMLModel, JSONModel

from .forms import TextModelForm


@admin.register(TextModel)
class TextModelAdmin(admin.ModelAdmin):
    form = TextModelForm


@admin.register(XMLModel)
class XMLModelAdmin(admin.ModelAdmin):
    pass


@admin.register(JSONModel)
class JSONModelAdmin(admin.ModelAdmin):
    pass
