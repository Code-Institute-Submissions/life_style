# Generated by Django 2.2.6 on 2020-02-22 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_course_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='start_time',
            field=models.CharField(choices=[('9.00', '9.00')], default='9.00', max_length=10),
            preserve_default=False,
        ),
    ]
