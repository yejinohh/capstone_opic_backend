from rest_framework import serializers
from .models import ImpromptuQuiz, SurveyQuiz

class ImpromptuQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImpromptuQuiz
        fields = ("__all__")

class SurveyQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyQuiz
        fields = ("__all__")

