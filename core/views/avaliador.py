from rest_framework.viewsets import ModelViewSet


from core.models import Avaliador
from core.serializers import AvaliadorSerializer



class AvaliadorViewSet(ModelViewSet):
    queryset = Avaliador.objects.all()
    serializer_class = AvaliadorSerializer

