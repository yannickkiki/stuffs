# Generated by Django 3.2.4 on 2021-07-15 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0002_alter_campaign_audience'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='namo',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
