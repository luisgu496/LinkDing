# Generated by Django 4.1 on 2023-01-09 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookmarks", "0018_bookmark_favicon_file"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="enable_favicons",
            field=models.BooleanField(default=False),
        ),
    ]