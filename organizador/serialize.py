from rest_framework import serializers
from . import models
from campeonato.models import Campeonato

class CampeonatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campeonato
        fields = ('id','nome','numero_times','imagem','regulamento')
        extra_kwargs = {'campeonatos': {'required': False}}

class OrganizadorSerializer(serializers.ModelSerializer):
    campeonatos = CampeonatoSerializer( many = True,required=False )
    class Meta:
        model = models.Organizador
        #fields = '__all__'
        fields = ('id','nome','sede','presidente','fundacao','imagem','campeonatos')    

