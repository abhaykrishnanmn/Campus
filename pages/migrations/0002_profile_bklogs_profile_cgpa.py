# Generated by Django 4.0.1 on 2023-02-24 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bklogs',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='cgpa',
            field=models.TextField(default=0.0),
            preserve_default=False,
        ),
    ]
