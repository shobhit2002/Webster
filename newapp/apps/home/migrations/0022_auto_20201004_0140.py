# Generated by Django 3.1 on 2020-10-03 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_notifications'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Notifications',
            new_name='Notification',
        ),
    ]