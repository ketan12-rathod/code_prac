# Generated by Django 4.2 on 2023-04-20 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0002_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sallary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sallary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myadmin.employee')),
            ],
            options={
                'db_table': 'sallary',
            },
        ),
    ]
