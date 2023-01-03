# Generated by Django 4.1.3 on 2023-01-03 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store_manager', '0064_alter_employe_request_form1_permanent_store_keeper_action'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employe_request_form1_permanent',
            name='Store_Keeper_Action',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approve', 'Approve'), ('Reject', 'Reject')], default='Pending', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='employe_request_form1_permanent',
            name='dept_head_Action',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Allowed', 'Allowed'), ('wait', 'wait'), ('Reject', 'Reject')], default='Pending', max_length=200, null=True),
        ),
    ]
