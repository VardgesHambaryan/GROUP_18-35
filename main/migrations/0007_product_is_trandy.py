# Generated by Django 5.0 on 2023-12-26 15:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0006_product_category_product_created_at_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="is_trandy",
            field=models.BooleanField(default=False),
        ),
    ]