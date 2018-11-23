MONACO_EDITOR_STATIC = {
    'js': (
        '/static/monaco/loader.js',
        '/static/djangoeditorwidgets/monaco/monaco.config.js',
    ),
    'css':  {
        'screen': ("/static/djangoeditorwidgets/monaco/monaco.custom.css", )
    }
}


TINYMCE_EDITOR_STATIC = {
    'js': (
        '/static/tinymce/tinymce.min.js',
        '/static/djangoeditorwidgets/tinymce/tinymce.config.js',
    ),
    'css': {
        'screen': ("/static/djangoeditorwidgets/tinymce/tinymce.custom.css", )
    }
}
