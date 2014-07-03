
from setuptools import setup

setup(
    name='django-jquery',
<<<<<<< HEAD
    version='1.5.10',
    url='https://github.com/AleXeY989/jquery.git',
    description='Django package for jquery-colorbox: A lightweight customizable lightbox plugin for jQuery',
    author='Jack Moore',
=======
    version='1.11.1',
    url='http://plugins.jquery.com/djangocsrf/',
    description='Django package for django-jquery: for jQuery',
    author='Baptiste Fontaine',
>>>>>>> ff8047c956758b37cea340d25c7d27b859407ac6
    maintainer='AleXeY989',
    maintainer_email='alex1chupahin@ya.ru',
    license='MIT License',
    keywords=['django', 'jquery'],
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
<<<<<<< HEAD
    packages=['django-jquery'],
    package_data={'django_jquery': ['static/django_jquery/js/*.js']}
=======
    packages=['django_jquery'],
    package_data={'django_jquery': ['static/js/django_jquery/*.js']}
>>>>>>> ff8047c956758b37cea340d25c7d27b859407ac6
)
