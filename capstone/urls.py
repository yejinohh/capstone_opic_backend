from django.urls import path, include
from .views import ImpromtumQuizAPI,  SurveyQuizAPI

urlpatterns = [
    path('impromptu/<int:id>/', ImpromtumQuizAPI),
    path('survey/<int:id>', SurveyQuizAPI),
]