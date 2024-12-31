# Generated by Django 3.2.6 on 2022-01-08 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookmarks", "0010_userprofile_bookmark_link_target"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="web_archive_integration",
            field=models.CharField(
                choices=[("disabled", "Disabled"), ("enabled", "Enabled")],
                default="disabled",
                max_length=10,
            ),
        ),
    ]
