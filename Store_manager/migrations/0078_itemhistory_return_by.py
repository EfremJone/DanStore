# Generated by Django 4.1.3 on 2023-01-25 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store_manager', '0077_itemhistory_other_reseaon'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemhistory',
            name='return_by',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
