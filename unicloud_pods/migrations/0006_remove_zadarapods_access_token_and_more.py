# Generated by Django 4.0.2 on 2022-06-15 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unicloud_pods', '0005_zadarapods_spare_nodes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zadarapods',
            name='access_token',
        ),
        migrations.AddField(
            model_name='zadarapods',
            name='domain_tenant',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='zadarapods',
            name='pod_password',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='zadarapods',
            name='pod_user',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
