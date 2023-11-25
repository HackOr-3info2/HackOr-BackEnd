from django.db import models

from .hackathon import Hackathon
from .user import User

class Avaliador (models.Model):
    nome = models.CharField(max_length=100)
    hackathon = models.ForeignKey(Hackathon, on_delete=models.PROTECT, related_name="avaliadores")
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="avaliadores")

    def __str__(self):
        return self.nome