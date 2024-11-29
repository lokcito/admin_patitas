from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Seed the database with initial data, including a superuser.'

    def handle(self, *args, **kwargs):
        # Configuración para el superusuario
        username = "admin"
        email = "admin@admin.com"
        password = "@123AbRaa"

        # Crear el superusuario si no existe
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" created successfully.'))
        else:
            self.stdout.write(self.style.WARNING(f'Superuser "{username}" already exists.'))

        # Puedes agregar más datos iniciales aquí si lo deseas.
        # Ejemplo:
        # from myapp.models import SomeModel
        # SomeModel.objects.create(name="Example")
        # self.stdout.write(self.style.SUCCESS("Initial data seeded successfully."))
