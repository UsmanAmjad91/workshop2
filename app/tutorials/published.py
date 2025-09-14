from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Tutorial
from .serializers import TutorialSerializer
@api_view(['GET'])
def tutorials_published(request):
    tutorials = Tutorial.objects.filter(published=True)
    serializer = TutorialSerializer(tutorials, many=True)
    return Response(serializer.data)
