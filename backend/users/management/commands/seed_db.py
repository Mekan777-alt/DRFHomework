from django.contrib.auth.models import Group
from django.core.management import BaseCommand

from users.enums import Groups


class Command(BaseCommand):
    def handle(self, *args, **options):
        Group.objects.get_or_create(name=Groups.BACKER.name)
        Group.objects.get_or_create(name=Groups.CREATOR.name)

        self.stdout.write('Groups added to database')
