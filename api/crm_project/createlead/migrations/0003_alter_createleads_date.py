# Generated by Django 5.1.1 on 2024-09-27 12:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createlead', '0002_alter_createleads_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createleads',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
