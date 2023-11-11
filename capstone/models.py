from django.db import models

class ImpromptuQuiz(models.Model):
    section = models.CharField(max_length=100, default="돌발주제")
    topic = models.CharField(max_length=100, default="")
    question = models.TextField()

class SurveyQuiz(models.Model):
    section = models.CharField(max_length=100, default="선택주제")
    topic = models.CharField(max_length=100, default="")
    question = models.TextField()

