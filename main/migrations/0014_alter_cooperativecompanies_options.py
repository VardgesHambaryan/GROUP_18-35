# Generated by Django 5.0 on 2023-12-28 15:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0013_product_discounted_price"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="cooperativecompanies",
            options={
                "verbose_name": "CooperativeCompanie",
                "verbose_name_plural": "CooperativeCompanies",
            },
        ),
    ]