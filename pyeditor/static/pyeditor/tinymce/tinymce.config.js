/* globals tinymce */

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
