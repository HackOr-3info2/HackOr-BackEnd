from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from core.views.comentario import ComentarioViewSet
from core.views.equipe import EquipeViewSet
from core.views.hackathon import HackathonViewSet
from core.views.user import UserViewSet
from core.views.tema import TemaViewSet
from core.views.avaliacao import AvaliacaoViewSet
from core.views.avaliador import AvaliadorViewSet
from core.views.categoria import CategoriaViewSet


from uploader.router import router as uploader_router

router = DefaultRouter()

router.register("users", UserViewSet, basename="users")
router.register("equipe", EquipeViewSet, basename="equipe")
router.register("hackathon", HackathonViewSet, basename="hackathon")
router.register("Temas", TemaViewSet, basename="temas")
router.register("comentario", ComentarioViewSet, basename="comentario")
router.register("avaliador", AvaliadorViewSet, basename="avaliador")
router.register("avaliacao", AvaliacaoViewSet, basename="avaliacao")
router.register("categoria", CategoriaViewSet, basename="categoria")


urlpatterns = [
    path("admin/", admin.site.urls),
    # OpenAPI 3
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("api/media/", include(uploader_router.urls)),
    
    # Simple JWT
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # API
    path("api/", include(router.urls)),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
