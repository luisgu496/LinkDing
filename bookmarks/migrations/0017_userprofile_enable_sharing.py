# Generated by Django 3.2.14 on 2022-08-04 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookmarks", "0016_bookmark_shared"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="enable_sharing",
            field=models.BooleanField(default=False),
        ),
    ]
