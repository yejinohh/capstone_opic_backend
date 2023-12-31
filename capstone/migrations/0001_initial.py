# Generated by Django 4.2.7 on 2023-11-05 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImpromptuQuiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(default='', max_length=100)),
                ('question', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SurveyQuiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(default='', max_length=100)),
                ('question', models.TextField()),
            ],
        ),
    ]
