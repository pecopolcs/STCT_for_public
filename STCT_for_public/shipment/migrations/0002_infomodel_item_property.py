# Generated by Django 3.0.2 on 2021-06-22 12:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='infomodel',
            name='item_property',
            field=models.CharField(default=django.utils.timezone.now, max_length=25),
            preserve_default=False,
        ),
    ]
