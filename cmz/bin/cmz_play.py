#!/usr/bin/env python
import os
import sys
import subprocess

if __name__ == "__main__":
    env = { "CMZ_WEBSITE_PATH" : os.getcwd() }
    env.update(os.environ)
    #manage_path = os.path.abspath("manage.py")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cmz.settings")

    print ">>>" * 4 + " WELCOME TO CMZ!"

    from django.core.management import execute_from_command_line

    execute_from_command_line(["migrate"])
    execute_from_command_line(["runserver"] + sys.argv)
