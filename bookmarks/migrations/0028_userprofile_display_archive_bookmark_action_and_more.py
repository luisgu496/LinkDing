# Generated by Django 5.0.2 on 2024-03-29 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookmarks", "0027_userprofile_bookmark_description_display_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="display_archive_bookmark_action",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="display_edit_bookmark_action",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="display_remove_bookmark_action",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="display_view_bookmark_action",
            field=models.BooleanField(default=True),
        ),
    ]
