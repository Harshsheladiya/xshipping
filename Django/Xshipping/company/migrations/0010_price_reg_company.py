# Generated by Django 5.0.4 on 2024-04-17 08:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0009_remove_price_reg_company'),
        ('myadmin', '0002_company_reg_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='price_reg',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myadmin.company_reg'),
        ),
    ]
