import pathlib

from django.apps import AppConfig
from django.conf import settings
from django.core.management import call_command


class DjangoEdirorWidgetsConfig(AppConfig):
    name = "djangoeditorwidgets"

    def ready(self):
        if not hasattr(settings, "WEB_EDITOR_DOWNLOAD"):
            raise Exception("'WEB_EDITOR_DOWNLOAD' is not defined in settings")

        WEB_EDITOR_DOWNLOAD = settings.WEB_EDITOR_DOWNLOAD
        WEB_EDITOR_CONFIG = settings.WEB_EDITOR_CONFIG

        to: pathlib.Path = WEB_EDITOR_DOWNLOAD["to"]
        editors = WEB_EDITOR_CONFIG.keys()

        if not all((to / ed).is_dir() for ed in editors):
            print("editor: downloading static files...")
            call_command("download_editor_scripts")
            print("editor: done.")
