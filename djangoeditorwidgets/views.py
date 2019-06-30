import mimetypes
import datetime as dt

from django.views.generic import View
from django.http import JsonResponse
from django.conf import settings



def assure_dir_exists(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def guess_type(url):
    t, _ = mimetypes.guess_type(url)
    if t is None:
        return ''
    return t.split('/')[0]


class FileUploadView(View):

    def parsefile(self, path, name):
        fullpath = os.path.join(path, name)

        info = {
            'name': name,
            'isdir': os.path.isdir(fullpath),
            'isimg': False,
            'url': fullpath.replace('%s/' % MEDIA_ROOT, '/'),
        }

        if not info['isdir']:
            extensions = [".jpg", ".jpeg", ".jfif", ".png", ".gif", ".svg"]

            if os.path.splitext(fullpath)[1].lower() in extensions:
                info['isimg'] = True

        return info

    def post(self, request, *args, **kwargs):
        MEDIA_ROOT = settings.MEDIA_ROOT

        files = request.FILES.getlist('files')
        upload_to = dt.datetime.now().strftime('uploads/%Y/%m-%d')
        assure_dir_exists(os.path.join(MEDIA_ROOT, upload_to))

        for file in files:
            try:
                path = os.path.join(MEDIA_ROOT, upload_to, file.name)
                chunks = list(file.chunks())[0]
                img = Image.open(io.BytesIO(chunks))
                img.save(path, optimize=True)
            except Exception:
                continue

            # DirName = os.path.dirname(path)
            # BaseName = os.path.basename(path)
            # item = self.parsefile(DirName, BaseName)

        return JsonResponse({
            # 'url': '/%s' % upload_to,
            # 'item': item
            "ok": True
        })
