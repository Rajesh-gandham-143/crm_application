# Generated by Django 5.1.1 on 2024-09-28 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createlead', '0003_alter_createleads_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createleads',
            name='Course',
            field=models.CharField(choices=[('HR Business Partner', 'HR Business Partner'), ('HR Generalist Core HR', 'HR Generalist Core HR'), ('HR Analytics', 'HR Analytics'), ('Spoken English', 'Spoken English'), ('Public Speaking', 'Public Speaking'), ('Communication Skills', 'Communication Skills'), ('Soft Skills', 'Soft Skills'), ('Personality Development', 'Personality Development'), ('Aptitude', 'Aptitude'), ('IELTS', 'IELTS'), ('TOEFL', 'TOEFL'), ('PTE', 'PTE'), ('GRE', 'GRE'), ('GMAT', 'GMAT'), ('Recruitment Specialist', 'Recruitment Specialist'), ('Payroll Specialist', 'Payroll Specialist'), ('Learning and Development', 'Learning and Development'), ('Others', 'Others'), ('Finance', 'Finance'), ('Competitive Exams', 'Competitive Exams'), ('HR Manage', 'HR Manage')], default='PTE', max_length=24),
        ),
        migrations.AlterField(
            model_name='createleads',
            name='TechStack',
            field=models.CharField(choices=[('Life Skills', 'Life Skills'), ('Study Abroad', 'Study Abroad'), ('HR', 'HR')], default='HR', max_length=24),
        ),
        migrations.AlterField(
            model_name='createleads',
            name='batch_timing',
            field=models.CharField(choices=[('7AM-8AM', '7AM-8AM'), ('8AM-9AM', '8AM-9AM'), ('9AM-10AM', '9AM-10AM'), ('10AM-11AM', '10AM-11AM'), ('11AM-12PM', '11AM-12PM'), ('12PM-1PM', '12PM-1PM'), ('1PM-2PM', '1PM-2PM'), ('2PM-3PM', '2PM-3PM'), ('3PM-4PM', '3PM-4PM'), ('4PM-5PM', '4PM-5PM'), ('5PM-6PM', '5PM-6PM'), ('6PM-7PM', '6PM-7PM'), ('7PM-8PM', '7PM-8PM'), ('8PM-9PM', '8PM-9PM')], default='7AM-8AM', max_length=10),
        ),
        migrations.AlterField(
            model_name='createleads',
            name='class_mode',
            field=models.CharField(choices=[('International Online', 'International Online'), ('India Online', 'India Online'), ('BLR Classroom', 'BLR Classroom'), ('HYD Classroom', 'HYD Classroom')], default='HYD Classroom', max_length=24),
        ),
        migrations.AlterField(
            model_name='createleads',
            name='lead_source',
            field=models.CharField(choices=[('None', 'None'), ('Walk In', 'Walk In'), ('Student Referral', 'Student Referral'), ('Demo', 'Demo'), ('Web Site', 'Web Site'), ('Web Site Chat', 'Web Site Chat'), ('Inbound Call', 'Inbound Call'), ('Google Ad Words', 'Google Ad Words'), ('Facebook Ads', 'Facebook Ads'), ('Google My Business', 'Google My Business'), ('WhatsApp Skill Capital', 'WhatsApp Skill Capital')], default='None', max_length=24),
        ),
    ]
