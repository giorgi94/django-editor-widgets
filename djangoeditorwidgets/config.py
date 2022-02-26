# WEB_EDITOR_STATICFILES = {
#     'monaco': {
#         'js': (
#             '/static/monaco/loader.js',
#             '/static/djangoeditorwidgets/monaco/monaco.config.js',
#         ),
#         'css': {
#             'screen': ("/static/djangoeditorwidgets/monaco/monaco.custom.css", )
#         }
#     },
#     'tinymce': {
#         'js': (
#             '/static/tinymce/tinymce.min.js',
#             '/static/djangoeditorwidgets/tinymce/tinymce.config.js',
#             '/static/djangoeditorwidgets/tinymce/tinymce.init.js',
#         ),
#         'css': {
#             'screen': ("/static/djangoeditorwidgets/tinymce/tinymce.custom.css", )
#         }
#     }
# }

WEB_EDITOR_DOWNLOAD = {
    "tinymce": {
        "url": "https://download.tiny.cloud/tinymce/community/tinymce_5.10.3.zip",
        "target": "/tinymce/js/tinymce",
    },
    "monaco": {
        "url": "https://registry.npmjs.org/monaco-editor/-/monaco-editor-0.32.1.tgz",
        "target": "/package/min/vs",
    },
}

WEB_EDITOR_CONFIG = {
    "tinymce": {
        "js": [
            "/static/tinymce/tinymce.min.js",
            "/static/djangoeditorwidgets/tinymce/tinymce.config.js",
            "/static/djangoeditorwidgets/tinymce/tinymce.init.js",
        ],
        "css": {
            "all": [
                "/static/djangoeditorwidgets/tinymce/tinymce.custom.css",
            ]
        },
    }
}
