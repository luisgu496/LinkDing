# Generated by Django 5.0.8 on 2024-09-18 20:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookmarks", "0039_globalsettings_enable_link_prefetch"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="items_per_page",
            field=models.IntegerField(
                default=30, validators=[django.core.validators.MinValueValidator(10)]
            ),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="sticky_pagination",
            field=models.BooleanField(default=False),
        ),
    ]
