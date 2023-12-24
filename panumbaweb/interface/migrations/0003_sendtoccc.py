# Generated by Django 4.2.7 on 2023-12-24 13:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("interface", "0002_alter_aicontact_answer"),
    ]

    operations = [
        migrations.CreateModel(
            name="SendToCCC",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("ip", models.CharField(max_length=100)),
                ("number", models.BigIntegerField(default=0)),
                (
                    "red",
                    models.IntegerField(
                        default=0,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(255),
                        ],
                    ),
                ),
                (
                    "green",
                    models.IntegerField(
                        default=0,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(255),
                        ],
                    ),
                ),
                (
                    "blue",
                    models.IntegerField(
                        default=0,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(255),
                        ],
                    ),
                ),
                ("token", models.CharField(max_length=100)),
            ],
        ),
    ]
