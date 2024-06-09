"""
Provides a simple API view that returns the authenticated user's information.

This view is protected by basic authentication and requires the user to be authenticated.

Args:
    request (django.http.request.HttpRequest): The incoming HTTP request.

Returns:
    rest_framework.response.Response: A JSON response containing the authenticated user's information.
"""
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([BasicAuthentication])
def user_api_view(request):
    return Response({'userInfo': str(request.user)})
