# Generated by Django 2.2.11 on 2020-10-08 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0023_auto_20201008_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsuggestion',
            name='customer_id_new',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='metacard',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='base.MetaCard'),
        ),
    ]
