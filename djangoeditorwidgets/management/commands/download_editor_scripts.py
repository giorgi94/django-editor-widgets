import os
import shutil
import tarfile
import zipfile
from os.path import basename
from pathlib import Path

import requests
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError


def is_within_directory(directory, target):

    abs_directory = os.path.abspath(directory)
    abs_target = os.path.abspath(target)

    prefix = os.path.commonprefix([abs_directory, abs_target])

    return prefix == abs_directory


def safe_extract(tar, path=".", members=None, *, numeric_owner=False):

    for member in tar.getmembers():
        member_path = os.path.join(path, member.name)
        if not is_within_directory(path, member_path):
            raise Exception("Attempted Path Traversal in Tar File")

    tar.extractall(path, members, numeric_owner=numeric_owner)


class Command(BaseCommand):
    help = "Download static files for editor widgets"

    def handle(self, *args, **options):

        if not hasattr(settings, "WEB_EDITOR_DOWNLOAD"):
            raise CommandError("Missing WEB_EDITOR_DOWNLOAD attribute in settings.py")

        self.read_config()

    def read_config(self):
        data: dict = settings.WEB_EDITOR_DOWNLOAD.copy()

        download_dir: Path = data.pop("to")

        for pkgname, pkgvalue in data.items():

            self.read_pkg(pkgname, pkgvalue, download_dir)

    def read_pkg(self, pkgname, pkgvalue, download_dir: Path):

        url = pkgvalue["url"]
        prefix = pkgvalue["target"].strip("/")

        pkgdir = download_dir / pkgname
        pkgdir.mkdir(exist_ok=True, parents=True)

        archive_file = pkgdir / "tmp" / basename(url)

        archive_file.parent.mkdir(exist_ok=True, parents=True)

        r = requests.get(url)

        archive_file.write_bytes(r.content)

        if zipfile.is_zipfile(archive_file):
            with zipfile.ZipFile(archive_file) as archive:
                archive.extractall(archive_file.parent)
        elif tarfile.is_tarfile(archive_file):
            with tarfile.open(archive_file) as archive:
                safe_extract(archive, archive_file.parent)
        else:
            return print("Cannot extract:", basename(url))

        prefixed = archive_file.parent / prefix

        for item in prefixed.iterdir():
            try:
                shutil.move(str(item), str(pkgdir))
            except shutil.Error as e:
                print("move eroor:", e)

        shutil.rmtree(str(archive_file.parent))
