from django.db import models
from .user import User
from .hackathon import Hackathon

class Comentario(models.Model):
    description = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name='comentarios', on_delete=models.CASCADE)
    hackathon = models.ForeignKey(Hackathon, related_name='comentarios', on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    liked = models.ManyToManyField(User, related_name='liked', blank=True)
    
    @property
    def likes(self):
        return self.liked.all().count()
    
LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),

)
    
class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comentario = models.ForeignKey(Comentario,on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES,default='Like', max_length=10)
    
    def __str__(self):
        return str(self.comentario)