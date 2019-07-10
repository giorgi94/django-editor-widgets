import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

setup(
    name='django-editor-widgets',
    version='2.0',
    packages=['djangoeditorwidgets'],
    description='Rich web editor widgets in the Django Admin',
    include_package_data=True,
    long_description=README,
    long_description_content_type="text/markdown",
    author='Giorgi Kakulashvili',
    # author_email='yourname@example.com',
    url='https://github.com/giorgi94/django-editor-widgets',
    keywords=['django', 'monaco', 'tinymce'],
    platforms=['OS Independent'],
    license='MIT',
    install_requires=[
        'Django>=2.0',
        'Pillow>=5.3.0'
    ]
)
