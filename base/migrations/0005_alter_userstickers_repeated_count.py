# Generated by Django 4.1 on 2022-09-05 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_userstickers_repeated_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstickers',
            name='repeated_count',
            field=models.IntegerField(default=0),
        ),
    ]
