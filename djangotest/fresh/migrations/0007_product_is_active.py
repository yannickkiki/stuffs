# Generated by Django 2.2.11 on 2021-05-13 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fresh', '0006_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
