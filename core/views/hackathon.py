from rest_framework.viewsets import ModelViewSet

from core.models import Hackathon
from core.serializers import HackathonSerializer


class HackathonViewSet(ModelViewSet):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer

