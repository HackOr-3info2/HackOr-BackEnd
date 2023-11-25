from django.db import models
from .user import User
from .hackathon import Hackathon

class Equipe(models.Model):
    name = models.CharField(max_length=255)
    tech = models.CharField(max_length=500)
    members = models.ManyToManyField(User, related_name='equipes')
    hackathon = models.ForeignKey(Hackathon, related_name="equipes", on_delete=models.PROTECT)

    def __str__(self):
        return self.name