# Generated by Django 3.2.5 on 2021-07-03 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientapp', '0007_auto_20210411_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='css_styles',
            field=models.CharField(blank=True, default='', max_length=512, null=True, verbose_name='Стили CSS'),
        ),
    ]