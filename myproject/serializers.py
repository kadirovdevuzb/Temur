from rest_framework import serializers
from .models import Yangiliklar, Filmlar

class YangiliklarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yangiliklar
        fields = ('__all__')

class FilmlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filmlar
        fields = ('__all__')