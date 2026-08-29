from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Genero (models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    

class Filme(models.Model):
    titulo = models.CharField(max_length=200)
    sinopse = models.TextField()
    lancamento = models.DateField()
    duracao = models.IntegerField()
    genero = models.ForeignKey(
        Genero,
        on_delete=models.CASCADE,
        related_name='filmes',
    )

    def __str__(self):
        return self.titulo

class Avaliacao(models.Model):
    nota = models.FloatField(validators=[
        MinValueValidator(0),
        MaxValueValidator(10),
        ])
    comentario = models.TextField(blank=True)
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,

    )
    filme = models.ForeignKey(
        Filme,
        on_delete=models.CASCADE,
        related_name='avaliacao',

    )

    def  __str__(self):
        return f'{self.filme.titulo} - {self.nota}/10'

