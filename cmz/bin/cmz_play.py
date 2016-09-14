#!/usr/bin/env python
import os
import sys
import subprocess

if __name__ == "__main__":
    env = { "CMZ_WEBSITE_PATH" : os.getcwd() }
    env.update(os.environ)
    #manage_path = os.path.abspath("manage.py")
    #os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cmz.settings")

    print ">>>" * 4 + " WELCOME TO CMZ!"

    manage_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "cmz_manage.py"))

    print ">>>" * 4 + " WELCOME TO CMZ!"

    subprocess.call([manage_path, "migrate"],
        env=env,
        #stdout=subprocess.PIPE,
    )

    subprocess.call([manage_path, "runserver"] + sys.argv[1:],
        env=env,
        #stdout=subprocess.PIPE,
    )
