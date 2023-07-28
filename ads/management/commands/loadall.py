from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand
from django.core.management import call_command

from users.models import User


class Command(BaseCommand):
    help = "Loads fixtures from fixtures dir"
    FIXTURES = {
        'location': 'users',
        'user': 'users',
        'category': 'ads',
        'ad': 'ads',
    }

    def handle(self, *args, **options):
        for fixture_name, app_label in self.FIXTURES.items():
            call_command('loaddata', fixture_name, app_label=app_label)

        for user in User.objects.all():
            user.password = make_password(user.password)
            user.save()
