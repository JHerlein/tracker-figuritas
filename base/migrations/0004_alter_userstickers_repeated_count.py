# Generated by Django 4.1 on 2022-09-05 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_userstickers_id_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstickers',
            name='repeated_count',
            field=models.IntegerField(null=True),
        ),
    ]
