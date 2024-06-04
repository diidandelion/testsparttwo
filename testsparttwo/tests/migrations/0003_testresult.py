# Generated by Django 5.0.6 on 2024-06-04 09:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tests", "0002_userdata"),
    ]

    operations = [
        migrations.CreateModel(
            name="TestResult",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("test_name", models.CharField(max_length=100)),
                ("result", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user_data",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="test_results",
                        to="tests.userdata",
                    ),
                ),
            ],
            options={
                "verbose_name": "Результат теста",
                "verbose_name_plural": "Результаты тестов",
            },
        ),
    ]
