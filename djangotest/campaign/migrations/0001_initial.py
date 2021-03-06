# Generated by Django 3.2.4 on 2021-07-15 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('audience', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('audience', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='segment.segment')),
            ],
            options={
                'db_table': 'campaign',
            },
        ),
    ]
