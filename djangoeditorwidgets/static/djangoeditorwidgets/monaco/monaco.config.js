/* global monaco */

document.addEventListener('DOMContentLoaded', function () {
    require.config({
        paths: {
            'vs': '/static/monaco/vs'
        }
    });

    var containers = Array.from(
        document.querySelectorAll('textarea[monaco-editor="true"]'));

    containers.forEach(function (container) {

        var form = container.form;

        var editorWrapper = document.createElement('div');
        editorWrapper.id = container.id + '--editor';
        editorWrapper.classList.add('monaco-editor--conteiner');

        require(['vs/editor/editor.main'], function () {
            try {
                container.style.display = 'none';
                container.parentElement.appendChild(editorWrapper);

                var editor = monaco.editor.create(document.getElementById(container.id + '--editor'), {
                    language: container.dataset.language,
                    wordWrap: container.dataset.wordwrap || 'off',
                    minimap: {
                        enabled: container.dataset.minimap === 'true'
                    },
                    fontSize: 12 + 1,
                    value: container.value
                });

                window[container.id + '_monaco_editor'] = editor;

                window.addEventListener('resize', function () {
                    editor.layout();
                });

                form.addEventListener('submit', function (e) {
                    container.value = editor.getValue();
                });
            } catch (err) {
                container.style.display = 'block';
                editorWrapper.remove();
            }
        });
    })

});