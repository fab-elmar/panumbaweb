from rest_framework.views import APIView
from rest_framework.response import Response
from panumbaweb.interface.models import AIcontact
from .serializers import AIcontactSerializer
from rest_framework.permissions import AllowAny


class LatestAnswerAPI(APIView):
    permission_classes = [AllowAny]
    def get(self, request, format=None):
        latest_answer = AIcontact.objects.latest('id')  
        serializer = AIcontactSerializer(latest_answer)
        return Response(serializer.data)
    
    
    
    