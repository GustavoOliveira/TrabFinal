from django.db import models

# Create your models here.
class Organizador (models.Model):
    nome= models.CharField(max_length=100)
    sede = models.CharField(max_length=100)
    presidente = models.CharField(max_length=100)
    fundacao = models.DateField(auto_now_add=False)
    imagem = models.FileField(blank=False, null=False)
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nome