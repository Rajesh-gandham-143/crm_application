# Generated by Django 5.1.1 on 2024-09-30 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createlead', '0004_alter_createleads_course_alter_createleads_techstack_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createleads',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
