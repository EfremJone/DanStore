# Generated by Django 4.1.3 on 2023-01-23 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Department_Head', '0005_dept_request_form1_permanent_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='dept_request_form1_permanent',
            name='Recival_status_by_Employer',
            field=models.CharField(choices=[('Received ', 'Received'), ('Not_Received ', 'Not_Received')], max_length=200, null=True),
        ),
    ]
