# Generated by Django 4.2 on 2023-05-11 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login',
            old_name='first_name',
            new_name='name',
        ),
    ]