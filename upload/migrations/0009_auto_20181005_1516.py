# Generated by Django 2.1.1 on 2018-10-05 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0008_auto_20181005_1510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='folder',
        ),
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to='files/needed_files/'),
        ),
    ]
