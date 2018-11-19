from rest_framework import serializers
from .models import Jogo

class JogoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Jogo