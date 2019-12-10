import string

from django.db import migrations
from django.contrib.auth import hashers


def create_test_users(apps, schema_editor):
    User = apps.get_model('auth', 'User')

    users = []
    for letter in string.ascii_uppercase:
        username = f'utilisateurtest{letter}'
        email = f'{username}@resolveneed.com'
        users.append(User(username=username, email=email, password=hashers.make_password(email)))

    User.objects.bulk_create(users)


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_create_super_user'),
    ]

    operations = [
        migrations.RunPython(create_test_users)
    ]
