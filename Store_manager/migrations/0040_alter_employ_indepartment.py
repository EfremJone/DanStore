# Generated by Django 4.1.3 on 2022-12-19 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store_manager', '0039_remove_employ_departments_employ_indepartment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employ',
            name='inDepartment',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
