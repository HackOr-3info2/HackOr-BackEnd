from rest_framework.serializers import ModelSerializer

from core.models import Avaliador


class AvaliadorSerializer(ModelSerializer):
    class Meta:
        model = Avaliador
        fields = "__all__"

