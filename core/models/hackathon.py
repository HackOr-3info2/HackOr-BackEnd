from django.db import models
from uploader.models import Image

from .equipe import Equipe
from .tema import Tema

#from .equipe import Equipe#



class Hackathon(models.Model):
    class Campi_Choices(models.IntegerChoices):
        AL=  1, 'Abelardo Luz'
        AR=  2, 'Araquari'
        BL=  3, 'Blumenau'
        BR=  4, 'Brusque'
        CA=  5, 'Camboriú'
        CO=  6, 'Concórdia'
        FR=  7, 'Fraiburgo '
        IB=  8, 'Ibirama'
        LU=  9, 'Luzerna'
        RS=  10, 'Rio do Sul' 
        SR=  11, 'Santa Rosa do Sul'
        SB=  12, 'São Bento do Sul'
        SF=  13, 'São Francisco do Sul'
        SO=  14, 'Sombrio '
        VI=  15, 'Videira'

    class status(models.IntegerChoices):
        PENDENTE = 1, "Pendente"
        EM_ANDAMENTO = 2, "Em Andamento"
        CONCLUIDO = 3, "Concluído"
        
    
    tema = models.ManyToManyField(Tema, related_name="hackathons")
    ano = models.DateField(null=True)
    campus = models.IntegerField(choices=Campi_Choices.choices)
    turma = models.CharField(max_length=100)
    estado = models.IntegerField(choices=status.choices)
    data_inicio = models.DateTimeField(null=True)
    data_final = models.DateTimeField(null=True)
    #equipes = models.ManyToManyField(Equipe, related_name='hackathons')#
    fotos = models.ManyToManyField(
        Image,
        related_name="+",

    )
    
    
    def __str__(self):
        return f"{self.get_campus_display()} {self.ano.year}"

