# Generated by Django 3.1 on 2020-10-12 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_auto_20201013_0320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='notification',
            name='message',
            field=models.TextField(default='', max_length=30),
        ),
    ]