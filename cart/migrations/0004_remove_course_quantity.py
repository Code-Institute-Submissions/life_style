# Generated by Django 2.2.6 on 2020-02-26 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_course_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='quantity',
        ),
    ]
