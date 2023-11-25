from django.db import models
from .user import User
from .categoria import Categoria
from .avaliador import Avaliador
from .equipe import Equipe

class Avaliacao(models.Model):    
    RATING_CHOICES = [
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]
    nota = models.CharField(max_length=1, choices=RATING_CHOICES, default='0')
    equipe = models.ForeignKey(Equipe, on_delete=models.PROTECT)
    avaliador = models.ForeignKey(Avaliador,on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    
    def __str__(self):
       return self.nota