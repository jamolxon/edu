# Generated by Django 5.0.4 on 2024-11-04 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_remove_attendance_lesson'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='day_type',
            field=models.CharField(choices=[('mwf', 'Monday, Wednesday, Friday'), ('tts', 'Tuesday, Thursday, Saturday')], null=True, verbose_name='day type'),
        ),
    ]
