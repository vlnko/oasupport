# Generated by Django 3.1.7 on 2021-04-11 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientapp', '0002_auto_20210411_1042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='company',
        ),
    ]
