from rest_framework.viewsets import ModelViewSet

from core.models import Tema
from core.serializers import TemaSerializer


class TemaViewSet(ModelViewSet):
    queryset = Tema.objects.all()
    serializer_class = TemaSerializer

