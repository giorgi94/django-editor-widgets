import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
readme = os.path.join(here, "README.md")

with open(readme) as fp:

    README = fp.read()

setup(
    name="django-editor-widgets",
    version="4.2",
    packages=["djangoeditorwidgets"],
    description="Rich web editor widgets in the Django Admin",
    include_package_data=True,
    long_description=README,
    long_description_content_type="text/markdown",
    author="Giorgi Kakulashvili",
    url="https://github.com/giorgi94/django-editor-widgets",
    keywords=["django", "monaco", "tinymce"],
    platforms=["OS Independent"],
    license="MIT",
    install_requires=["Django>=3.0", "Pillow>=8", "requests>=2"],
)
