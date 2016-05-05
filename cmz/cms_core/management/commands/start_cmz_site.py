import os, shutil
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

class Command(BaseCommand):
    help = 'Starts a new cmz project!'

    def add_arguments(self, parser):
        parser.add_argument('folder', type=str, default=".")

    def handle(self, *args, **options):
        path = os.path.abspath(options['folder'])
        website_path = os.path.join(path, 'website')
        if (os.path.isdir(website_path)):
            raise CommandError('"website" folder exists in %s -- refusing to go on.' % path)

        template_path = os.path.join(settings.BASE_DIR, "example_website/website")
        shutil.copytree(template_path, website_path)        

        self.stdout.write(self.style.SUCCESS('Successfully created website in : %s ' % website_path))
        self.stdout.write(self.style.SUCCESS('Now just run cmz_play.py and enjoy'))




        #raise CommandError('Poll "%s" does not exist' % poll_id)

            
        #self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))