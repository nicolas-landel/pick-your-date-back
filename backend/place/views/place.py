from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
# from django.contrib.auth.models import User
from place.models import Place
from place.serializers import PlaceSerializer

class PlaceViews(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]
    model = Place
    serializer_class = PlaceSerializer

    def get(self, request, format=None):
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)