# Generated by Django 4.1 on 2022-09-12 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_userstickers_country_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userstickers',
            old_name='repeated_count',
            new_name='count',
        ),
    ]
