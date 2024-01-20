from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand
from projects.models import CountryProject
from users.enums import Groups, Country

PROJECT_PERMISSION = Permission.objects.filter(codename__contains='project')

GROUP_PERMISSION_MAP = {
    Groups.CREATOR.name: PROJECT_PERMISSION
}

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.seed_groups()
        self.set_permissions()
        self.seed_country()

    def seed_country(self):
        CountryProject.objects.get_or_create(country_name=Country.RUSSIA.name)
        CountryProject.objects.get_or_create(country_name=Country.USA.name)
        CountryProject.objects.get_or_create(country_name=Country.SPAIN.name)
        CountryProject.objects.get_or_create(country_name=Country.TURKEY.name)
        CountryProject.objects.get_or_create(country_name=Country.GB.name)

        self.stdout.write('Country added to database')

    def seed_groups(self):
        Group.objects.get_or_create(name=Groups.BACKER.name)
        Group.objects.get_or_create(name=Groups.CREATOR.name)

        self.stdout.write('Groups added to database')

    def set_permissions(self):
        for group, permissions in GROUP_PERMISSION_MAP.items():
            group = Group.objects.get(name=group)
            group.permissions.set(permissions)

        self.stdout.write('Permissions set for groups')
