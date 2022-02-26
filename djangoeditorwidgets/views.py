import datetime as dt
import io
import mimetypes
import os

from django.conf import settings
from django.http import JsonResponse
from django.views.generic import View
from PIL import Image


def assure_dir_exists(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def guess_type(url):
    t, _ = mimetypes.guess_type(url)
    if t is None:
        return ""
    return t.split("/")[0]


class FileUploadView(View):

    upload_to = "uploads/%Y/%m-%d"

    def post(self, request, *args, **kwargs):
        MEDIA_URL = str(settings.MEDIA_URL)
        MEDIA_ROOT = str(settings.MEDIA_ROOT)

        file = request.FILES.get("file")
        upload_to = dt.datetime.now().strftime(self.upload_to)
        assure_dir_exists(os.path.join(MEDIA_ROOT, upload_to))

        try:
            path = os.path.join(MEDIA_ROOT, upload_to, file.name)
            path = self.upload_handler(file, path)

            return JsonResponse({"url": path.replace(MEDIA_ROOT + "/", MEDIA_URL)})
        except Exception as ex:
            print(ex)
            return JsonResponse({"error": str(ex)})

    def upload_handler(self, file, path):
        filename, ext = os.path.splitext(path)
        seconds = str(eval(dt.datetime.now().strftime("3600*%H+60*%M+%S")))
        seconds = "0" * (5 - len(seconds)) + seconds
        path = filename + "-" + seconds + ext

        chunks = list(file.chunks())[0]

        img = Image.open(io.BytesIO(chunks))
        img.save(path, optimize=True)

        return path
