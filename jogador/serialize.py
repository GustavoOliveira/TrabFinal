from rest_framework import serializers
from .models import Jogador

class JogadorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Jogador
        
        