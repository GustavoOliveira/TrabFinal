from django.db import models
from organizador.models import Organizador

# Create your models here.
class Campeonato (models.Model):
    nome= models.CharField(max_length=100)
    numero_times = models.IntegerField()
    organizador = models.ForeignKey(Organizador, related_name='campeonatos', on_delete=models.CASCADE)
    imagem = models.FileField(blank=False, null=False)
    regulamento = models.FileField(blank=False, null=False)
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nome
