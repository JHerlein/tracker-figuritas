# Generated by Django 4.1 on 2022-09-05 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstickers',
            name='has',
            field=models.BooleanField(default=False),
        ),
    ]
