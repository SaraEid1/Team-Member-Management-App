# Generated by Django 4.0 on 2021-12-16 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=250)),
                ('lastname', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('phone_number', models.IntegerField(max_length=10)),
            ],
        ),
    ]
