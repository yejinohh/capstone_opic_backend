# Generated by Django 4.2.7 on 2023-11-05 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0002_delete_surveyquiz'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ImpromptuQuiz',
            new_name='Quiz',
        ),
    ]