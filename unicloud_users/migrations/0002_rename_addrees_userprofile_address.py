# Generated by Django 4.0.2 on 2022-04-01 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unicloud_users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='addrees',
            new_name='address',
        ),
    ]
