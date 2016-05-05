#!/usr/bin/env python
import os
import shutil
import sys
import subprocess

import example_website


if __name__ == "__main__":
    env = { "CMZ_WEBSITE_PATH" : os.getcwd() }
    
    print ">>>" * 2 + " Creating new cmz website"

    path = os.getcwd()
    website_path = os.path.join(path, 'website')
    if (os.path.isdir(website_path)):
        print ">>>" * 2 + ' CMZ Error :(  '
        print ">>>" * 2 + ' "website" folder exists in %s -- refusing to go on.' % path
        print
        #raise Exception(')
        sys.exit(1)

    template_path = os.path.join(os.path.dirname(example_website.__file__), "website")
    shutil.copytree(template_path, website_path)        
    
    print ">>>" * 2 + ' Successfully created website in : %s ' % website_path
    print ">>>" * 2 + ' Now just run cmz_play.py and enjoy :)'
    print

    
    

    
