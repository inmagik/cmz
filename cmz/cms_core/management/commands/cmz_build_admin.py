import os, shutil
from distutils.sysconfig import get_python_lib
from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import site
import logging
import importlib
import imp
# Get an instance of a logger
logger = logging.getLogger(__name__)



class Command(BaseCommand):
    help = 'Prepare admin configuration'

    #TODO: THIS SHOULD COME FROM A CONFIG VAR IN SETTINGS
    def get_admin_path(self):
        BASE_DIR = settings.BASE_DIR

        top_path =  os.path.abspath(os.path.join(BASE_DIR, "../"))
        cmz_admin_path_devel = os.path.join(top_path, "cmz-admin")

        CMZ_ADMIN_PATH = None
        if os.path.isdir(cmz_admin_path_devel):
            CMZ_ADMIN_PATH = cmz_admin_path_devel
        else:
            #installed in a virtualenv or site-packages directory
            site_packages_path = get_python_lib()
            cmz_admin_path_site_packages = os.path.abspath(os.path.join(site_packages_path, "../cmz-admin"))
            if os.path.isdir(cmz_admin_path_devel):
                CMZ_ADMIN_PATH = cmz_admin_path_site_packages
            else:
                #logger.warning('NO ADMIN DIR FOUND')
                raise CommandError("Cannot find admin dir")

        return  os.path.abspath(os.path.join(CMZ_ADMIN_PATH, 'ng2-admin/src/app/pages/symlinks'))


    def handle(self, *args, **options):
        #get the current location of the admin
        cmz_admin_path = self.get_admin_path()

        if os.path.isdir(cmz_admin_path):
            shutil.rmtree(cmz_admin_path)
        os.mkdir(cmz_admin_path)

        for app in settings.SITE_MODULES:
            try:
                app_path = importlib.import_module(app).__path__
            except AttributeError:
                continue

            cmz_admin_module_path = os.path.abspath(os.path.join(app_path[0],"cmz-admin"))
            if os.path.isdir(cmz_admin_module_path):
                cmz_admin_config = os.path.join(cmz_admin_module_path, "admin-config.json")
                if os.path.isfile(cmz_admin_config):
                    #LINK FILE

                    target = os.path.join(cmz_admin_path, app )
                    print "link", target, app
                    logger.info("Linking app %s" % app)
                    os.symlink(cmz_admin_module_path, target)

            logger.info("No cmz-admin for app %s" % app)
