# Generated by Django 5.0.7 on 2024-08-06 17:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("listings", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listing",
            name="logo",
            field=models.ImageField(blank=True, upload_to="company-logos/"),
        ),
    ]
