from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = "Run all migrations and create a default superuser"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("Running migrations..."))
        call_command("migrate")

        User = get_user_model()
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "admin@example.com", "adminpass123")
            self.stdout.write(self.style.SUCCESS("Created superuser: admin / adminpass123"))
        else:
            self.stdout.write(self.style.WARNING("Superuser already exists"))
