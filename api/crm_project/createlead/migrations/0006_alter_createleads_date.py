# Generated by Django 5.1.1 on 2024-10-01 09:40

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createlead', '0005_alter_createleads_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createleads',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
