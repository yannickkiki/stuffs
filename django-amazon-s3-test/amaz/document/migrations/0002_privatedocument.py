# Generated by Django 3.1.4 on 2020-12-03 14:10

import config.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivateDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(storage=config.storage.PrivateMediaStorage(), upload_to='')),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
