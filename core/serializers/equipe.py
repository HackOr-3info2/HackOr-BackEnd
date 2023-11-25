from rest_framework.serializers import ModelSerializer

from core.models import Equipe


class EquipeSerializer(ModelSerializer):
    class Meta:
        model = Equipe
        fields = "__all__"
