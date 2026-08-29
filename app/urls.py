from rest_framework.routers import DefaultRouter

from .viewsets import GeneroViewset,FilmeViewset,AvaliacaoViewset


router = DefaultRouter()

router.register('generos',  GeneroViewset)
router.register('filmes', FilmeViewset)
router.register('avaliacoes', AvaliacaoViewset)

urlpatterns = router.urls