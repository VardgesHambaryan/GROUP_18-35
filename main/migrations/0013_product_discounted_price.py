# Generated by Django 5.0 on 2023-12-28 15:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0012_rename_is_trandy_product_is_trendy_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="discounted_price",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=10,
                null=True,
                verbose_name="Discounted Price",
            ),
        ),
    ]
