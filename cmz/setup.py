#!/usr/bin/env python

from setuptools import setup
from setuptools import find_packages

setup(name='cmz',
      version='0.1',
      description='INMAGIK cms',
      author='INMAGIK',
      author_email='bianchimro@gmail.com',
      #url='https://www.python.org/sigs/distutils-sig/',
      #packages=["cmz.cms_content", "cmz.cms_core", "cmz.cms_news", "cmz.cmz", "cmz.cms_theme_bootstrap"],
      packages = find_packages("cmz"),
      include_package_data=True,
      scripts = ["./cmz_play.py", "./cmz_start.py" ,"./manage.py" ],
      install_requires=['Django==1.9.5',  'django-activelink',
      'django-classy-tags==0.7.2', 'django-sekizai==0.9.0', 'wheel==0.26.0'],

      dependency_links=['https://github.com/gbozee/django-activelink/tarball/c31619ceb0fe16d96adae524fb44a8b135d85597.tar.gz#egg=django_activelink']
    )
