WEB_EDITOR_STATICFILES = {
    'monaco': {
        'js': (
            '/static/monaco/loader.js',
            '/static/djangoeditorwidgets/monaco/monaco.config.js',
        ),
        'css': {
            'screen': ("/static/djangoeditorwidgets/monaco/monaco.custom.css", )
        }
    },
    'tinymce': {
        'js': (
            '/static/tinymce/tinymce.min.js',
            '/static/djangoeditorwidgets/tinymce/tinymce.config.js',
            '/static/djangoeditorwidgets/tinymce/tinymce.init.js',
        ),
        'css': {
            'screen': ("/static/djangoeditorwidgets/tinymce/tinymce.custom.css", )
        }
    }
}
