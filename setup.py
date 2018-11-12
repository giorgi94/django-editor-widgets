import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

setup(
    name='django-web-editors',
    version='0.1',
    packages=['pyeditor'],
    description='A line of description',
    long_description=README,
    author='yourname',
    author_email='yourname@example.com',
    # url='https://github.com/yourname/django-myapp/',
    license='MIT',
    install_requires=[
        'Django>=1.11,<=2',
    ]
)
