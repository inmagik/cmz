#!/usr/bin/env python
import os
import sys
import subprocess

if __name__ == "__main__":
    env = { "CMZ_WEBSITE_PATH" : os.getcwd() }
    env.update(os.environ)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cmz.settings")
    os.environ.setdefault("CMZ_WEBSITE_PATH", os.getcwd() )
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
