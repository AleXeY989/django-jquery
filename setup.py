
from setuptools import setup

setup(
    name='django-jquery',
    version='1.11.1',
    url='http://plugins.jquery.com/djangocsrf/',
    description='Django package for django-jquery: for jQuery',
    author='Baptiste Fontaine',
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
    packages=['django_jquery'],
    package_data={'django_jquery': ['static/js/django_jquery/*.js']}
)
