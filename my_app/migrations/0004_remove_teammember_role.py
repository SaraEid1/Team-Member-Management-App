# Generated by Django 4.0 on 2021-12-16 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_teammember_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammember',
            name='role',
        ),
    ]
