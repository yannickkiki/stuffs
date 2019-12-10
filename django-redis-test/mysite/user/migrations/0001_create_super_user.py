from django.db import migrations
from django.contrib.auth import hashers


def create_super_user(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    User.objects.create(
        username='almeki',
        password=hashers.make_password('mele-alya-kikico'),
        is_superuser=True,
        is_staff=True
    )


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.RunPython(create_super_user)
    ]
