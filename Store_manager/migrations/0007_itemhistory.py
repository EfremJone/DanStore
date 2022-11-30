# Generated by Django 4.1.3 on 2022-11-29 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Store_manager', '0006_alter_item_catagory'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Reason', models.CharField(blank=True, max_length=200, null=True)),
                ('Action', models.CharField(choices=[('New_Add', 'New_Add'), ('Removed', 'Removed')], max_length=200)),
                ('Approved', models.CharField(blank=True, max_length=200, null=True)),
                ('last_update', models.DateField(auto_now_add=True)),
                ('Item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Store_manager.item')),
            ],
        ),
    ]
