from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import OsintResult
from .serializers import OsintResultSerializer
from .services.maigret_service import search_username_and_store


@api_view(['GET'])
def search_username(request, username):
    if request.method == 'GET':
        try:
            osint_result = OsintResult.objects.get(username=username)
        except OsintResult.DoesNotExist:
            osint_result = search_username_and_store(username=username,
                                                     tags=['gb'], json_file='simple')
        # result = search_username2(username)
        serializer = OsintResultSerializer(osint_result)
        return Response(serializer.data, status=status.HTTP_200_OK)
