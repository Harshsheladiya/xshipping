# Generated by Django 5.0.4 on 2024-04-20 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0022_remove_orderinfo_selected_company_name_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='companyorder',
            table='CompanyOrder',
        ),
    ]
