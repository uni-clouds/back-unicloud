# Generated by Django 4.0.6 on 2022-07-18 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unicloud_contracts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contracts',
            name='customer',
        ),
    ]
