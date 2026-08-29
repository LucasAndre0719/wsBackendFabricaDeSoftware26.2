from django.test import TestCase
from django.contrib.auth.models import User
from .serializers import AvaliacaoSerializers

from .models import Genero, Filme, Avaliacao


class FilmeTestCase(TestCase):

    def setUp(self):
        self.usuario = User.objects.create_user(
            username='usuario_teste',
            password='123456'
        )

        self.genero = Genero.objects.create(
            nome='Ação'
        )

        self.filme = Filme.objects.create(
            titulo='Filme Teste',
            sinopse='Um filme para teste',
            lancamento='2026-01-01',
            duracao=120,
            genero=self.genero
        )

    def test_filme_criado(self):
        self.assertEqual(self.filme.titulo, 'Filme Teste')
        self.assertEqual(self.filme.duracao, 120)

    def test_avaliacao_criada(self):
        avaliacao = Avaliacao.objects.create(
            nota=10,
            comentario='Excelente filme!',
            usuario=self.usuario,
            filme=self.filme
        )

        self.assertEqual(avaliacao.nota, 10)
        self.assertEqual(avaliacao.usuario, self.usuario)
        self.assertEqual(avaliacao.filme, self.filme)

    def test_usuario_nao_pode_avaliar_filme_duas_vezes(self):
        Avaliacao.objects.create(
            nota=10,
            comentario='Primeira avaliação',
            usuario=self.usuario,
            filme=self.filme
        )

        avaliacao = AvaliacaoSerializers(
            data={
                'nota': 8,
                'comentario': 'Segunda avaliação',
                'filme': self.filme.id
            },
            context={
                'request': type(
                    'Request',
                    (),
                    {'user': self.usuario}
                )()
            }
        )

        self.assertFalse(avaliacao.is_valid())

        self.assertIn(
            'Voce já avaliou este filme.',
            str(avaliacao.errors)
        )
    def test_nota_deve_ser_entre_0_e_10(self):
        avaliacao = AvaliacaoSerializers(
        data={
            'nota': 11,
            'comentario': 'Nota inválida',
            'filme': self.filme.id
        },
        context={
            'request': type(
                'Request',
                (),
                {'user': self.usuario}
            )()
        }
    )

        self.assertFalse(avaliacao.is_valid())
        self.assertIn('nota', avaliacao.errors)