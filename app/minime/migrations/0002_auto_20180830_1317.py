# Generated by Django 2.1 on 2018-08-30 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minime', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url',
            name='count',
        ),
        migrations.AddField(
            model_name='url',
            name='password',
            field=models.CharField(max_length=1024, null=True),
        ),
    ]
