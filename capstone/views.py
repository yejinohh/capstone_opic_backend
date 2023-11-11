from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import ImpromptuQuiz, SurveyQuiz
from .serializers import ImpromptuQuizSerializer, SurveyQuizSerializer  # Corrected the typo

@api_view(['GET'])
def ImpromtumQuizAPI(request, id):
    quiz = ImpromptuQuiz.objects.get(id=id)
    serializer = ImpromptuQuizSerializer(quiz)  # Correct serializer
    return Response(serializer.data, content_type='application/json; charset=utf-8')

    
@api_view(['GET'])
def SurveyQuizAPI(request, id):
    quiz = SurveyQuiz.objects.get(id=id)
    serializer = SurveyQuizSerializer(quiz)  # Serialize multiple objects
    return Response(serializer.data, content_type='application/json; charset=utf-8')

