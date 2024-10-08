# Generated by Django 5.1 on 2024-08-13 19:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("listings", "0002_alter_listing_logo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listing",
            name="logo",
            field=models.ImageField(
                blank=True,
                default="company-logos/default-logo.png",
                upload_to="company-logos/",
            ),
        ),
    ]
