#!/usr/bin/env python
import sys
from setuptools import setup
from setuptools import find_packages
import os

with open("requirements.txt", "rb") as requirements:
    lines = requirements.readlines()
    install_requires = [x.replace("\n", "") for x in lines]



setup(name='cmz',
      version='0.1',
      description='INMAGIK cms',
      author='INMAGIK',
      author_email='bianchimro@gmail.com',
      #url='https://www.python.org/sigs/distutils-sig/',
      #packages=["cmz.cms_content", "cmz.cms_core", "cmz.cms_news", "cmz.cmz", "cmz.cms_theme_bootstrap"],
      packages = find_packages('cmz'),
      package_dir={'':'cmz'},
      include_package_data=True,
      scripts = ["cmz/bin/cmz_play.py", "cmz/bin/cmz_start.py" , "cmz/bin/cmz_manage.py", "cmz/manage.py" ],
      install_requires=install_requires,

      #dependency_links=['git+https://github.com/gbozee/django-activelink.git@c31619ceb0fe16d96adae524fb44a8b135d85597#egg=django_activelink']
    )
