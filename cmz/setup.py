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
      packages = find_packages("."),
      include_package_data=True,
      scripts = ["cmz_play.py", "manage.py" ],
      install_requires=['Django==1.9.5', 'django-activelink==0.4',
      'django-classy-tags==0.7.2', 'django-sekizai==0.9.0', 'wheel==0.26.0'],
    )
