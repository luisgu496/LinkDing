# Generated by Django 5.0.2 on 2024-04-01 12:17

from django.db import migrations
from django.contrib.auth import get_user_model

from bookmarks.models import Toast

User = get_user_model()


def forwards(apps, schema_editor):

    for user in User.objects.all():
        toast = Toast(
            key="html_snapshots_hint",
            message="This version adds a new feature for archiving snapshots of websites locally. To use it, you need to switch to a different Docker image. See the installation instructions on GitHub for details.",
            owner=user,
        )
        toast.save()


def reverse(apps, schema_editor):
    Toast.objects.filter(key="bookmark_list_actions_hint").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("bookmarks", "0031_userprofile_enable_automatic_html_snapshots"),
    ]

    operations = [
        migrations.RunPython(forwards, reverse),
    ]
