/* globals tinymce */


/*
(function () {
    var selectedImage = null;

    var tinymceConfig = {
        selector: 'textarea[tinymce-editor]',
        height: 300,
        paste_as_text: true,
        force_p_newlines: true,
        invalid_elements: 'br,div',
        cleanup: true,
        plugins: ['advlist autolink lists link image charmap print preview anchor', 'searchreplace visualblocks code fullscreen', 'insertdatetime media table contextmenu paste imagetools', 'wordcount', 'textcolor colorpicker', 'codesample', 'pagebreak'],
        toolbar: 'insertfile undo redo | styleselect | forecolor backcolor fontsizeselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | codesample link media image | browse | fullscreen | pagebreak',
        fontsize_formats: '8pt 10pt 12pt 14pt 18pt 24pt 36pt',
        codesample_languages: [
            { text: 'HTML/XML', value: 'markup' },
            { text: 'JavaScript', value: 'javascript' }
        ],
        fontsize_width: 30,
        image_caption: true,
        relative_urls: false,
        images_upload_url: '/media/',
        init_instance_callback: function (editor) {
            editor.getBody().style.fontSize = '15px';

            editor.on('click', function () {
                var node;
                node = tinymce.activeEditor.selection.getNode();
                if (node.tagName === 'IMG' && node.getAttribute('src').indexOf('blob:') === -1) {
                    selectedImage = node.getAttribute('src');
                    return selectedImage;
                }
            });
        },
        setup: function (editor) {
            editor.addButton('browse', {
                title: 'Insert files',
                icon: 'browse',
                onclick: function () {
                    fileBrowserCallback('id_content_ifr', 'files', 'type', window);
                    return console.log('fileBrowserCallback');
                }
            });
            return editor.on('SaveContent', function (event) {
                event.content = event.content.replace(/&nbsp;/g, ' ').replace(/\s{2,}/g, ' ');
                return event.content;
            });
        },
        images_upload_handler: function (blobInfo, success, failure) {
            var filename, form;
            filename = blobInfo.filename();
            if (filename.indexOf('imagetool') === 0) {
                filename = selectedImage;
            }
            form = new FormData();
            form.append('image', blobInfo.blob());
            form.append('filename', filename);
            // return UploadFile(`${window.__MEDIA_MANAGER_PATH__}file_upload_handler`, form).then(function (res) {
            //     if (!res.data.failure) {
            //         return success(res.data.success);
            //     } else {
            //         return failure();
            //     }
            // }).catch(function (err) {
            //     return failure();
            // });
        },
        file_browser_callback: function (fieldname, url, type, win) {
            console.log(fieldname, url, type, win);
            return fileBrowserCallback(fieldname, url, type, win);
        }
    };

    var fileBrowserCallback = function (fieldname, url, type, win) {
        var mediaManager;
        mediaManager = window.__MEDIA_MANAGER_PATH__;
        return tinymce.activeEditor.windowManager.open({
            file: mediaManager,
            title: 'Media Manager',
            width: 1000,
            height: 600,
            resizable: 'yes',
            plugins: 'media',
            inline: 'yes',
            close_previous: 'no'
        }, {
            window: win,
            input: fieldname
        });
    };

    tinymceConfig;
    tinymce.init(tinymceConfig);
})();
*/

(function (options) {

    if (!options) {
        options = {};
    }

    options = {
        media_manager_url: null,
        content_css: [],
        images_upload_url: '/media/',
        ...options
    }


    const media_manager_url = options.media_manager_url;


    let config = {
        selector: 'textarea[tinymce-editor]',
        height: 500,
        paste_as_text: true,
        force_p_newlines: true,
        invalid_elements: 'br',
        menubar: true,
        contextmenu: false,
        fontsize_width: 30,
        content_css: options.content_css,
        plugins: [
            'advlist', 'autolink', 'lists', 'link', 'image', 'charmap',
            'print', 'preview', 'anchor', 'searchreplace', 'visualblocks',
            'code', 'fullscreen', 'imagetools',
            'codesample', 'pagebreak', 'insertdatetime',
            'media', 'table', 'paste', 'code', 'help', 'wordcount',
        ],
        toolbar: `
            insertfile undo redo | styleselect | fontsizeselect |  forecolor backcolor
            | bold italic underline | alignleft aligncenter alignright alignjustify
            | bullist numlist outdent indent
            | codesample link | media image browse | fullscreen | pagebreak`,
        setup(editor) {

            if (media_manager_url) {
                editor.ui.registry.addButton('browse', {
                    title: 'Insert files',
                    icon: 'browse',
                    onAction: () => alert('Button clicked!')
                });
            }



            editor.on('SaveContent', function (event) {
                event.content = event.content
                    .replace(/&nbsp;/g, ' ').replace(/\s{2,}/g, ' ');
                return event.content;
            });
        },
    }

    config = {
        ...config,
        image_caption: true,
        relative_urls: false,
        images_upload_url: options.images_upload_url,
        images_upload_handler(blobInfo, success, failure) {
            imageUploadHandler(blobInfo, success, failure)
        },
    }


    if (media_manager_url) {
        config = {
            ...config,
            file_picker_types: 'file image media',
            file_picker_callback(callback, value, meta) {
                browseFiles(value, meta.filetype, (fileUrl) => callback(fileUrl));
            }
        }
    }

    const imageUploadHandler = (blobInfo, success, failure) => {

        console.log(blobInfo, success, failure)

        /*
        var xhr, formData;

        xhr = new XMLHttpRequest();
        xhr.withCredentials = false;
        xhr.open('POST', 'postAcceptor.php');

        xhr.onload = function () {
            var json;

            if (xhr.status != 200) {
                failure('HTTP Error: ' + xhr.status);
                return;
            }

            json = JSON.parse(xhr.responseText);

            if (!json || typeof json.location != 'string') {
                failure('Invalid JSON: ' + xhr.responseText);
                return;
            }

            success(json.location);
        };

        formData = new FormData();
        formData.append('file', blobInfo.blob(), blobInfo.filename());

        xhr.send(formData);
        */
    }

    const browseFiles = (value, filetype, callback) => {

        tinymce.activeEditor.windowManager.openUrl({
            title: 'Media Manager',
            url: media_manager_url || '/',
            buttons: [],
            onAction(instance, trigger) {
                instance.close();
            },
            width: 600,
            height: 300
        });
    }

    tinymce.init(config);
})(window.tinymceOptions)