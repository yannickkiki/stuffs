# Generated by Django 3.2.4 on 2021-07-08 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fresh', '0008_auto_20210513_1119'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductProxy',
            fields=[
            ],
            options={
                'managed': False,
                'proxy': True,
            },
            bases=('fresh.product',),
        ),
    ]
