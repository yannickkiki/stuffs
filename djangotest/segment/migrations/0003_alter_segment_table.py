# Generated by Django 3.2.4 on 2021-07-15 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('segment', '0002_alter_segment_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='segment',
            table='audience',
        ),
    ]