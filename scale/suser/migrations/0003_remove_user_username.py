# Generated by Django 3.2.4 on 2021-07-01 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suser', '0002_remove_user_getting_report'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
