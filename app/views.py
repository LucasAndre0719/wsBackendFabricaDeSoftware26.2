from django.shortcuts import render
import requests

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET'])
def filmes_externos(request):

    url = 'https://www.swapi.tech/api/films/'

    try:
        resposta = requests.get(url, timeout=5)

        if resposta.status_code != 200:
            return Response(
                {
                'erro': 'não foi possivel consultar a API'
                },
                status= status.HTTP_502_BAD_GATEWAY
            )

        dados = resposta.json()

        return Response(dados,status=status.HTTP_200_OK)
    except request.RequestException:
        return Response(
            {
                'erro': 'Erro ao conectar com a API externa' 
            }, 
            status= status.HTTP_503_SERVICE_UNAVAILABLE
        )


    

# Create your views here.
