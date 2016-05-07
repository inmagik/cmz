import os, shutil
from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings



#print os.environ['CMZ_STATIC_PATH']


class Command(BaseCommand):
    help = 'Starts a new cmz project!'


    def handle(self, *args, **options):
        #call_command('staticsitegen')
        env = {}
        env.update(os.environ)
        env['CMZ_STATIC_PATH'] = 'static'
        #call_command('collectstatic', '--noinput', env=env)
        os.environ.setdefault("CMZ_STATIC_PATH", "static")
        from django.core.management import execute_from_command_line
        execute_from_command_line(["manage.py", "staticsitegen"] )
        execute_from_command_line(["manage.py", "collectstatic"] )
