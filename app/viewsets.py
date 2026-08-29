from rest_framework import viewsets
from .models import Genero,Filme,Avaliacao

from .serializers import GeneroSerializers,FilmeSerializers,AvaliacaoSerializers


class GeneroViewset(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializers


class FilmeViewset(viewsets.ModelViewSet):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializers

class AvaliacaoViewset(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializers

    