from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import OsintResult
from .serializers import OsintResultSerializer, UserSerializer
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


class CreateUserView(APIView):
    
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            email = serializer.validated_data['email']
            phone_number = serializer.validated_data['phone_number']
            # Perform any additional processing or database operations here
            return Response({'message': 'User created successfully'})
        return Response(serializer.errors, status=400)
