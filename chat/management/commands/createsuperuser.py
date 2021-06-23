from django.contrib.auth.management.commands import createsuperuser
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from chat.models import Blacklist


class Command(createsuperuser.Command):
    def handle(self, *args, **options):
        super().handle(*args, **options)
        try:  # TODO: this never executes if superuser was not created, no need for try-catch clause
            superuser = User.objects.get(username=self.username)
            Blacklist.objects.create(owner=superuser)
        except ObjectDoesNotExist:
            print("Error: superuser was not created")

    def get_input_data(self, field, message, default=None):
        input_data = super().get_input_data(field, message, default=default)
        if message in ("Username: ", "Username (leave blank to use 'root'): "):
            self.username = input_data if input_data else default
        return input_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.username = None
