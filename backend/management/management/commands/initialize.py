from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Initialize the database'

    def handle(self, *args, **options):
        self.stdout.write('Initializing the database...')
        self.stdout.write('Done.')