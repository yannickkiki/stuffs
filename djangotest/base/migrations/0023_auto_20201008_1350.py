# Generated by Django 2.2.11 on 2020-10-08 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0022_auto_20201008_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='metacard',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='base.MetaCard'),
        ),
        migrations.AlterField(
            model_name='productsuggestion',
            name='account',
            field=models.IntegerField(),
        ),
    ]
