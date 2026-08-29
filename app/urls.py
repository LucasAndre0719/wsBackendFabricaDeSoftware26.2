from rest_framework.routers import DefaultRouter
from .viewsets import GeneroViewset,FilmeViewset,AvaliacaoViewset
from django.urls import path
from .views import filmes_externos



router = DefaultRouter()

router.register('generos',  GeneroViewset)
router.register('filmes', FilmeViewset)
router.register('avaliacoes', AvaliacaoViewset)

urlpatterns = router.urls

urlpatterns+=[
    path ('filmes_externos/', filmes_externos),
]