from rest_framework import serializers
from .models import Genero,Filme,Avaliacao


class GeneroSerializers (serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'

class FilmeSerializers(serializers.ModelSerializer):
    duracao = serializers.IntegerField(min_value = 1)
    class Meta:
        model = Filme
        fields = '__all__'

class AvaliacaoSerializers(serializers.ModelSerializer):
    nota = serializers.FloatField(min_value = 0, max_value = 10)
    class Meta:
        model = Avaliacao
        fields = ['id', 'nota', 'comentario', 'usuario', 'filme']
        read_only_fields = ['usuario']
    def validate(self, data):
        usuario = self.context['request'].user
        filme = data.get('filme')

        if Avaliacao.objects.filter(usuario = usuario, filme = filme).exists():
            raise serializers.ValidationError('Voce já avaliou este filme.')
        return data
    

class FilmeExternoSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    titulo = serializers.CharField()
    diretor = serializers.CharField()
    produtor = serializers.CharField()
    lancamento=serializers.DateField()
    sinopse = serializers.CharField()