# Generated by Django 4.0.5 on 2023-02-25 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_rename_bklogs_profile_bklgs'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='addr',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='codechef',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='github',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='linkedin',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='stkoflw',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='website',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
