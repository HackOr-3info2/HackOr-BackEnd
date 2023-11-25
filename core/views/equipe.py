from rest_framework.viewsets import ModelViewSet

from core.models import Equipe
from core.serializers import EquipeSerializer


class EquipeViewSet(ModelViewSet):
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer

