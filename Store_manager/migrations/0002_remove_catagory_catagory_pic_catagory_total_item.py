# Generated by Django 4.1.3 on 2022-11-28 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store_manager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catagory',
            name='Catagory_pic',
        ),
        migrations.AddField(
            model_name='catagory',
            name='total_item',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
