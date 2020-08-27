from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):

    help = "this command creates users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="How many users do you want to create?",
        )

    def handle(self, *args, **options):
        admin = User.objects.get_or_none(username="ebadmin")
        if not admin:
            User.objects.create_superuser("ebadmin", "kim1120318@naver.com", "1234")
            self.stdout.write(self.style.SUCCESS("SuperUser Created"))
        else:
            self.stdout.write(self.style.SUCCESS("SuperUser Exist"))

