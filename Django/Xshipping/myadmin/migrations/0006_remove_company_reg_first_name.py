# Generated by Django 5.0.4 on 2024-04-23 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0005_rename_fname_company_reg_first_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company_reg',
            name='first_name',
        ),
    ]