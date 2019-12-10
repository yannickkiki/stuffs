from django.db import migrations
from django.contrib.auth import hashers


def create_super_user(apps, schema_editor):
    User = apps.get_model('user', 'User')
    db_alias = schema_editor.connection.alias
    User.objects.using(db_alias).create(
        username='yannoveli',
        password=hashers.make_password('yannoveli'),
        is_superuser=True,
        is_staff=True
    )


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_super_user)
    ]
