# Generated by Django 4.1.3 on 2023-02-02 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store_manager', '0081_remove_form2permanent_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='form2permanent',
            name='Admin_response',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='allstore',
            name='storeKeeper',
            field=models.CharField(default='TBA', max_length=300),
        ),
    ]