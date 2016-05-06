#!/usr/bin/env python
import os
import sys
import subprocess

if __name__ == "__main__":
    env = { "CMZ_WEBSITE_PATH" : os.getcwd() }
    env.update(os.environ)
    manage_path = "manage.py"

    print ">>>" * 4 + " WELCOME TO CMZ!"

    subprocess.call([manage_path, "migrate"], 
        env=env,
        #stdout=subprocess.PIPE,
    )
    
    subprocess.call([manage_path, "runserver"] + sys.argv[1:], 
        env=env,
        #stdout=subprocess.PIPE,
    )

    
