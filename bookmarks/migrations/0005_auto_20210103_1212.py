# Generated by Django 2.2.13 on 2021-01-03 12:12

import bookmarks.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookmarks", "0004_auto_20200926_1028"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookmark",
            name="url",
            field=models.CharField(
                max_length=2048,
                validators=[bookmarks.validators.BookmarkURLValidator()],
            ),
        ),
    ]
