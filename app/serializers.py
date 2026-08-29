from rest_framework import serializers
from .models import Genero,Filme,Avaliacao


class GeneroSerializers (serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'

class FilmeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = '__all__'

class AvaliacaoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = '__all__'

        