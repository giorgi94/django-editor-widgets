/* global monaco */

/*
# Monaco Editor Interface:
https://microsoft.github.io/monaco-editor/api/interfaces/monaco.editor.idiffeditorconstructionoptions.html

# Monaco Editor Theme Example:
https://github.com/microsoft/monaco-editor/blob/master/test/playground.generated/customizing-the-appearence-exposed-colors.html
*/


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


                monaco.editor.defineTheme('myTheme', {
                    base: 'vs',
                    inherit: true,
                    rules: [{ background: 'FFFFFF' }],
                    colors: {
                        'editor.lineHighlightBackground': '#00A1FF0F'
                    }
                });
                monaco.editor.setTheme('myTheme');

                var editor = monaco.editor.create(document.getElementById(container.id + '--editor'), {
                    renderWhitespace: true,
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