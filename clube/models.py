from django.db import models
from campeonato.models import Campeonato

# Create your models here.
class Clube (models.Model):
    nome= models.CharField(max_length=100)
    criacao = models.DateField(auto_now_add=False)
    pontuacao = models.IntegerField()
    campeonato = models.ForeignKey(Campeonato, related_name='clubes', on_delete=models.CASCADE)
    escudo = models.FileField(blank=False, null=False)
    hino = models.FileField(blank=False, null=False)
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nome