# Generated by Django 2.1.1 on 2018-10-05 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0005_auto_20181005_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to='files/needed_files/'),
        ),
    ]
