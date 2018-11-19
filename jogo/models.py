from django.db import models

# Create your models here.
class Jogo (models.Model):
    time_casa = models.IntegerField()
    time_fora = models.IntegerField()
    gol_tm_casa = models.IntegerField()
    gol_tm_fora = models.IntegerField()
    data = models.DateField(auto_now_add=False)    
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nome