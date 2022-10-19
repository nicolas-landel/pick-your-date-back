from backend.place.models.place import Place
from rest_framework import serializers
from place.models import Place

class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = '__all__',
        read_only = ["created_at", "pk"]