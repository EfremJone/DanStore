# Generated by Django 4.1.3 on 2023-01-13 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_unaproved_employees_cheek'),
    ]

    operations = [
        migrations.AddField(
            model_name='unaproved_employees',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
