# Generated by Django 3.1.2 on 2020-11-09 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parcel_id', models.CharField(max_length=20)),
                ('parcel_address', models.CharField(max_length=30)),
                ('parcel_city', models.CharField(max_length=20)),
                ('parcel_zip', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ParcelGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('members', models.ManyToManyField(to='parcels.Parcel')),
            ],
        ),
    ]
