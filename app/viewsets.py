from rest_framework import viewsets
from .models import Genero,Filme,Avaliacao
from rest_framework.permissions import IsAuthenticated
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
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Avaliacao.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
