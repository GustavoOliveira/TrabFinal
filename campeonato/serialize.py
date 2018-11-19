from rest_framework import serializers
from .models import Campeonato
from clube.models import Clube

class ClubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clube
        fields = ('id','nome','criacao','pontuacao','escudo','hino')

class CampeonatoSerializer(serializers.ModelSerializer):
    clubes = ClubeSerializer( many = True ,required=False)
    class Meta:
        fields = ('id','nome','numero_times','imagem','regulamento','organizador','clubes')
        model = Campeonato
        