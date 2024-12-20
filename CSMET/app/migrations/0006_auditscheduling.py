# Generated by Django 4.2.2 on 2023-07-20 05:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0005_alter_auditinitiation_station"),
    ]

    operations = [
        migrations.CreateModel(
            name="auditscheduling",
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
                ("auditschedulingyear", models.IntegerField(null=True)),
                (
                    "file_upload",
                    models.FileField(default=None, upload_to="auditscheduling/"),
                ),
                ("unit", models.CharField(max_length=80, null=True)),
                ("station", models.CharField(max_length=80, null=True)),
                ("auditfrom", models.DateField(max_length=80, null=True)),
                ("auditto", models.DateField(max_length=80, null=True)),
            ],
        ),
    ]
