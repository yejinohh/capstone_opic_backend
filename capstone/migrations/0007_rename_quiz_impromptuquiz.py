# Generated by Django 4.2.7 on 2023-11-10 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0006_remove_surveyquiz_section_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Quiz',
            new_name='ImpromptuQuiz',
        ),
    ]
