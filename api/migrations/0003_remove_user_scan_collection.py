# Generated by Django 4.2.7 on 2023-12-18 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='scan_collection',
        ),
    ]
