from django.http import JsonResponse
from rest_framework.views import APIView


# TODO use rest_framework.generics GenericAPIView -> see doc https://github.com/encode/django-rest-framework/blob/master/rest_framework/generics.py
class ListView(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]
    model = None
    serializer = None
    queryset = None

    def get_queryset(self):
        return self.queryset.all()

    def get(self, request, format=None):
        serializer = self.serializer(self.get_queryset(), many=True)
        return JsonResponse(serializer.data, safe=False)


class GetView(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]
    model = None
    serializer = None
    queryset = None

    def get_object(self, uuid):
        return self.queryset.get(uuid=uuid)

    def get(self, request, format=None):
        uuid = request.uuid
        if not uuid:
            raise KeyError("No uuid in the request")
        instance = self.get_object(uuid)
        serializer = self.serializer(instance)
        return JsonResponse(serializer.data, safe=False)
