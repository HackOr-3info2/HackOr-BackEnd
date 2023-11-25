from rest_framework.serializers import ModelSerializer

from core.models import Tema


class TemaSerializer(ModelSerializer):
    class Meta:
        model = Tema
        fields = "__all__"
