# Generated by Django 2.2.13 on 2021-02-14 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookmarks", "0005_auto_20210103_1212"),
    ]

    operations = [
        migrations.AddField(
            model_name="bookmark",
            name="is_archived",
            field=models.BooleanField(default=False),
        ),
    ]