# Generated by Django 2.2.14 on 2023-12-07 17:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gritmakerApp', '0005_remove_sensordata_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensordata',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
