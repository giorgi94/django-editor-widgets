const tinymceConfig = ({ name, media_upload_url, media_manager_url }) => {
    let config = {
        selector: `textarea[data-tinymce="${name}"]`,
        height: 500,
        paste_as_text: true,
        force_p_newlines: true,
        invalid_elements: "br",
        menubar: true,
        contextmenu: false,
        fontsize_width: 30,
        content_css: [],
        plugins: [
            "advlist",
            "autolink",
            "lists",
            "link",
            "image",
            "charmap",
            "print",
            "preview",
            "anchor",
            "searchreplace",
            "visualblocks",
            "code",
            "fullscreen",
            "imagetools",
            "codesample",
            "pagebreak",
            "insertdatetime",
            "media",
            "table",
            "paste",
            "code",
            "help",
            "wordcount",
        ],
        toolbar: `
            insertfile undo redo | styleselect | fontsizeselect |  forecolor backcolor
            | bold italic underline | alignleft aligncenter alignright alignjustify
            | bullist numlist outdent indent
            | link media image browse | pagebreak codesample | fullscreen`,
        setup(editor) {
            editor.on("SaveContent", function (event) {
                event.content = event.content
                    .replace(/&nbsp;/g, " ")
                    .replace(/\s{2,}/g, " ");
                return event.content;
            });

            if (media_manager_url) {
                editor.ui.registry.addButton("browse", {
                    title: "Insert files",
                    icon: "browse",
                    onAction: () => alert("Button clicked!"),
                });
            }
        },
    };

    const imageUploadHandler = (blobInfo, success, failure) => {
        let xhr, formData;

        xhr = new XMLHttpRequest();
        xhr.withCredentials = false;
        xhr.open("POST", media_upload_url);

        xhr.onload = function () {
            let json;

            if (xhr.status < 200 || xhr.status >= 300) {
                console.log(json);
                return failure("HTTP Error: " + xhr.status);
            }

            json = JSON.parse(xhr.responseText);

            if (!json || !json.url || json.error) {
                console.log(json);
                return failure("Faild to Upload Image");
            }

            return success(json.url);
        };

        formData = new FormData();
        formData.append(
            "csrfmiddlewaretoken",
            document.querySelector('input[name="csrfmiddlewaretoken"]').value
        );
        formData.append("file", blobInfo.blob(), blobInfo.filename());

        xhr.send(formData);
    };

    const browseFiles = (value, filetype, callback) => {
        tinymce.activeEditor.windowManager.openUrl({
            title: "Media Manager",
            url: media_manager_url,
            buttons: [],
            onAction(instance, trigger) {
                instance.close();
            },
            width: 600,
            height: 300,
        });
    };

    if (media_upload_url) {
        config = {
            ...config,
            image_caption: true,
            relative_urls: false,
            images_upload_url: "/media/",
            images_upload_handler(blobInfo, success, failure) {
                imageUploadHandler(blobInfo, success, failure);
            },
        };
    }

    if (media_manager_url) {
        config = {
            ...config,
            file_picker_types: "file image media",
            file_picker_callback(callback, value, meta) {
                browseFiles(value, meta.filetype, (fileUrl) =>
                    callback(fileUrl)
                );
            },
        };
    }

    return config;
};
