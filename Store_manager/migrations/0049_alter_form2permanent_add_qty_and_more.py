# Generated by Django 4.1.3 on 2022-12-19 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store_manager', '0048_rename_reqqty_form2permanent_req_qty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form2permanent',
            name='add_qty',
            field=models.IntegerField(blank=True, default='0', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='form2permanent',
            name='req_qty',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
    ]
