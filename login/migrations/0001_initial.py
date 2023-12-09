# Generated by Django 4.2.7 on 2023-12-08 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Account",
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
                ("username", models.CharField(max_length=20, verbose_name="用户名")),
                ("password", models.CharField(max_length=20, verbose_name="密码")),
                ("gender", models.IntegerField(default=0, verbose_name="性别")),
            ],
        ),
    ]