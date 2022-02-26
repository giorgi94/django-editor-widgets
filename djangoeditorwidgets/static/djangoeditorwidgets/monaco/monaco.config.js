document.addEventListener("DOMContentLoaded", function () {
    require.config({
        paths: {
            vs: "/static/monaco/vs",
        },
    });

    const containers = Array.from(
        document.querySelectorAll("textarea[data-monaco]")
    );

    containers.forEach(function (container) {
        const form = container.form;

        const editorWrapper = document.createElement("div");

        editorWrapper.id = container.id + "--editor";
        editorWrapper.classList.add("monaco-editor--conteiner");

        require(["vs/editor/editor.main"], function () {
            try {
                container.style.display = "none";
                container.parentElement.appendChild(editorWrapper);

                monaco.editor.defineTheme("myTheme", {
                    base: "vs",
                    inherit: true,
                    rules: [{ background: "FFFFFF" }],
                    colors: {
                        "editor.lineHighlightBackground": "#00A1FF0F",
                    },
                });
                monaco.editor.setTheme("myTheme");

                const editor = monaco.editor.create(
                    document.getElementById(container.id + "--editor"),
                    {
                        language: container.dataset.language || "html",
                        wordWrap: container.dataset.wordwrap || "off",
                        minimap: {
                            enabled: container.dataset.minimap == "on",
                        },
                        fontSize: 14,
                        value: container.value,
                        automaticLayout: true,
                        renderWhitespace: true,
                        scrollBeyondLastLine: true,
                    }
                );

                window[container.id + "_monaco_editor"] = editor;

                window.addEventListener("resize", function () {
                    editor.layout();
                });

                form.addEventListener("submit", function (e) {
                    container.value = editor.getValue();
                });
            } catch (err) {
                container.style.display = "block";
                editorWrapper.remove();
            }
        });
    });
});
