# Generated by Django 2.1.1 on 2018-10-05 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0012_auto_20181005_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to='files/needed_files/'),
        ),
    ]
