from os.path import join
from pathlib import PosixPath


def init_web_editor_config(download_dir: PosixPath, static_url: str):

    download_dir.mkdir(exist_ok=True, parents=True)

    WEB_EDITOR_DOWNLOAD = {
        "to": download_dir,
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
                join(static_url, "tinymce/tinymce.min.js"),
                join(static_url, "djangoeditorwidgets/tinymce/tinymce.config.js"),
                join(static_url, "djangoeditorwidgets/tinymce/tinymce.init.js"),
            ],
            "css": {
                "all": [
                    join(static_url, "djangoeditorwidgets/tinymce/tinymce.custom.css"),
                ]
            },
        },
        "monaco": {
            "js": [
                join(static_url, "monaco/vs/loader.js"),
                join(static_url, "djangoeditorwidgets/monaco/monaco.config.js"),
            ],
            "css": {
                "all": [
                    join(static_url, "djangoeditorwidgets/monaco/monaco.custom.css"),
                ]
            },
        },
    }

    return WEB_EDITOR_DOWNLOAD, WEB_EDITOR_CONFIG
