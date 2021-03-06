# Generated by Django 4.0.6 on 2022-07-22 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unicloud_customers', '0006_remove_customerrequest_customer_and_more'),
        ('unicloud_contracts', '0002_remove_contracts_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContractParty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='unicloud_contracts.contracts')),
                ('contractor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='organization_contractor', to='unicloud_customers.customer')),
                ('hired', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='organization_hired', to='unicloud_customers.customer')),
            ],
        ),
        migrations.RemoveField(
            model_name='customercontracts',
            name='contract',
        ),
        migrations.RemoveField(
            model_name='customercontracts',
            name='customer',
        ),
        migrations.DeleteModel(
            name='Contractor',
        ),
        migrations.DeleteModel(
            name='CustomerContracts',
        ),
    ]
