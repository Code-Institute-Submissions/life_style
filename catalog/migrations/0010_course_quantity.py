# Generated by Django 2.2.6 on 2020-02-26 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20200225_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
