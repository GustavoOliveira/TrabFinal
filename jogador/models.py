from django.db import models
from clube.models import Clube

# Create your models here.
class Jogador (models.Model):
    nome= models.CharField(max_length=100)
    idade = models.IntegerField()
    time = models.ForeignKey(Clube, related_name='jogadores', on_delete=models.CASCADE)
    peso = models.FloatField()
    foto = models.FileField(blank=False, null=False)
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nome