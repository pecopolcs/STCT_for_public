# Generated by Django 3.0.2 on 2021-06-23 02:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shipment', '0002_infomodel_item_property'),
    ]

    operations = [
        migrations.AddField(
            model_name='infomodel',
            name='consignee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
