# Generated by Django 4.0.6 on 2022-07-22 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unicloud_contracts', '0003_contractparty_remove_customercontracts_contract_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contracts',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]