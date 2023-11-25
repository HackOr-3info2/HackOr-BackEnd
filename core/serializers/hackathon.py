from rest_framework.serializers import ModelSerializer

from core.models import Hackathon


class HackathonSerializer(ModelSerializer):
    class Meta:
        model = Hackathon
        fields = "__all__"

