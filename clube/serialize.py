from rest_framework import serializers
from .models import Clube
from jogador.models import Jogador

class JogadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogador
        fields = ('id','nome','idade','time','peso','foto')

class ClubeSerializer(serializers.ModelSerializer):
    jogadores = JogadorSerializer( many = True,required=False )
    class Meta:
        fields = ('id','nome','criacao','pontuacao','campeonato','escudo','hino','jogadores')
        model = Clube