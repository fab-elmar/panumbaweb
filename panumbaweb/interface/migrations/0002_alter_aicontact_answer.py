# Generated by Django 4.2.7 on 2023-12-17 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("interface", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aicontact",
            name="answer",
            field=models.BigIntegerField(default=0),
        ),
    ]
