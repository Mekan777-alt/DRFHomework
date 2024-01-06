from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand

from users.enums import Groups

PROJECT_PERMISSION = Permission.objects.filter(codename__contains='project')

GROUP_PERMISSION_MAP = {
    Groups.CREATOR.name: PROJECT_PERMISSION
}

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.seed_groups()
        self.set_permissions()

    def seed_groups(self):
        Group.objects.get_or_create(name=Groups.BACKER.name)
        Group.objects.get_or_create(name=Groups.CREATOR.name)

        self.stdout.write('Groups added to database')

    def set_permissions(self):
        for group, permissions in GROUP_PERMISSION_MAP.items():
            group = Group.objects.get(name=group)
            group.permissions.set(permissions)

        self.stdout.write('Permissions set for groups')
