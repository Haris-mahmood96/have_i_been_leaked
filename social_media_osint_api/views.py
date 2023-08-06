from datetime import timedelta

from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import UsernameOsintResult, EmailOsintResult
from .serializers import OsintResultSerializer, EmailOsintSerializer
from .services.emailosint.email_osint import search_email
from .services.maigret_service import search_username_and_store


def ordered_to_regular_dict(data):
    if isinstance(data, dict):
        return {k: ordered_to_regular_dict(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [ordered_to_regular_dict(v) for v in data]
    elif isinstance(data, object):
        try:
            return {k: ordered_to_regular_dict(v) for k, v in vars(data).items()}
        except TypeError:
            return data
    else:
        return data


@api_view(['GET'])
def search_username(request, username):
    if request.method == 'GET':
        try:
            osint_result: UsernameOsintResult = UsernameOsintResult.objects.get(username=username)
        except UsernameOsintResult.DoesNotExist:
            osint_result = search_username_and_store(username=username,
                                                     tags=['gb'], json_file='simple')
        # result = search_username2(username)
        serializer = OsintResultSerializer(osint_result)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def email_osint_analysis(request):
    email = request.data.get("email")

    # Get the refresh_rate header, or use '60' as a default
    refresh_rate: float = float(request.headers.get('refresh_rate', '3'))

    if not email:
        return Response({"detail": "Email is missing."}, status=status.HTTP_400_BAD_REQUEST)

    # Check if user with given email already exists
    try:
        email_osint: EmailOsintResult = EmailOsintResult.objects.get(email=email)
        email_osint.leaks = ordered_to_regular_dict(email_osint.leaks)
        email_osint.basic_email_reputation = ordered_to_regular_dict(email_osint.basic_email_reputation)
        email_osint.social_media_registrations = ordered_to_regular_dict(email_osint.social_media_registrations)

        # check if the search_results were more than 3 days ago then update the database.
        # A refresh rate of 3 days is used because Breach Director API has a limit of 10 request per month,
        # so on average we can make a call every 3 days

        if email_osint.updated_at < timezone.now() - timedelta(days=refresh_rate):
            search_results = search_email(email)
            #  merging two dictionaries via the unpacking operator **,  If the same key exists in both ,
            #  the value from search results is used.

            email_osint.leaks = {**email_osint.results, **search_results.get("leaks")}
            email_osint.save()
    except EmailOsintResult.DoesNotExist:
        # If user does not exist, create a new one
        search_results = search_email(email)
        serializer = EmailOsintSerializer(data=search_results)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # If user with given email already exists, return the user data
    serializer = EmailOsintSerializer(email_osint)

    return Response(serializer.data)
