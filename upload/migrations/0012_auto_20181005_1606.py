# Generated by Django 2.1.1 on 2018-10-05 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0011_auto_20181005_1526'),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to=''),
        ),
    ]
