import jwt
from rest_framework_jwt.utils import jwt_payload_handler, jwt_encode_handler
from rest_framework_simplejwt import tokens
from isi_test_project.settings import SECRET_KEY
from django.core.management.base import BaseCommand, CommandError
from django.db.utils  import IntegrityError
from accounts.models import CustomUser


class Command(BaseCommand):
    help = "Create a custom user"

    def add_arguments(self, parser):
        for arg in ["username", "password"]:
            parser.add_argument(arg)

    def handle(self, *args, **options):
        try:
            user = CustomUser.objects.create_user(
                username=options["username"], password=options["password"]
            )
            token = jwt_encode_handler(
                jwt_payload_handler(user)
            )
            self.stdout.write(
                self.style.SUCCESS(str(token))
            )
        except IntegrityError as ex:
            raise CommandError(ex)
