# Generated by Django 4.2.7 on 2023-11-10 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0005_remove_surveyquiz_id_surveyquiz_surveyquiz_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveyquiz',
            name='section',
        ),
        migrations.RemoveField(
            model_name='surveyquiz',
            name='surveyquiz_id',
        ),
        migrations.AddField(
            model_name='surveyquiz',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
