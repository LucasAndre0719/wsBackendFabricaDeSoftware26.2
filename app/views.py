from django.shortcuts import render
import requests

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from drf_spectacular.utils import extend_schema, OpenApiParameter

@extend_schema(
    parameters=[
        OpenApiParameter(
            name='titulo',
            description='Filtra os filmes pelo título',
            required=False,
            type=str
        )
    ]
)
@api_view(['GET'])
def filmes_externos(request):

    url = 'https://www.swapi.tech/api/films/'

    titulo = request.query_params.get('titulo')

    try:
        resposta = requests.get(url, timeout=5)

        if resposta.status_code != 200:
            return Response(
                {
                    'erro': 'Não foi possível consultar a API'
                },
                status=status.HTTP_502_BAD_GATEWAY
            )

        try:
            dados = resposta.json()

        except ValueError:
            return Response(
                {
                    'erro': 'A API externa retornou uma resposta inválida.'
                },
                status=status.HTTP_502_BAD_GATEWAY
            )

        filmes = dados.get('result', [])

        if titulo:
            filmes_filtrados = []

            for filme in filmes:
                nome_filme = filme.get('properties', {}).get('title', '')

                if titulo.lower() in nome_filme.lower():
                    filmes_filtrados.append(filme)

            filmes = filmes_filtrados

        if titulo and not filmes:
            return Response(
                {
                    'erro': f'Nenhum filme encontrado para "{titulo}".'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(
            filmes,
            status=status.HTTP_200_OK
        )

    except requests.RequestException:
        return Response(
            {
                'erro': 'Erro ao conectar com a API externa'
            },
            status=status.HTTP_503_SERVICE_UNAVAILABLE
        )