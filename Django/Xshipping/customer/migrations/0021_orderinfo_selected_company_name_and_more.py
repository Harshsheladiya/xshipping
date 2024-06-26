# Generated by Django 5.0.4 on 2024-04-20 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0020_remove_orderinfo_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='selected_company_name',
            field=models.CharField(default='SomeDefaultValue', max_length=255),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='selected_company_price',
            field=models.DecimalField(decimal_places=2, default='0.0', max_digits=10),
        ),
    ]
