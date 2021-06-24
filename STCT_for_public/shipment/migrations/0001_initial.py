# Generated by Django 3.0.2 on 2021-06-21 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InfoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipper_name', models.CharField(max_length=25)),
                ('depdate_from_ru', models.DateField()),
                ('spec_no', models.CharField(max_length=12)),
                ('cntr_no', models.CharField(max_length=12)),
                ('cube_m3', models.FloatField()),
                ('cntr_eta', models.DateField()),
                ('vessel_name', models.CharField(max_length=25)),
                ('bool_eta', models.BooleanField(default=False)),
                ('final_update', models.DateField()),
                ('option', models.TextField()),
            ],
        ),
    ]