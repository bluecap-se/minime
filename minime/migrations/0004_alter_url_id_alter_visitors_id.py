# Generated by Django 4.1.1 on 2022-10-01 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("minime", "0003_visitors"),
    ]

    operations = [
        migrations.AlterField(
            model_name="url",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="visitors",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
