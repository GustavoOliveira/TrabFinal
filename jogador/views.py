from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Jogador
from .serialize import JogadorSerializer
from rest_framework.permissions import IsAuthenticated

class JogadorList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Jogador.objects.all()
    serializer_class = JogadorSerializer

class JogadorDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = Jogador.objects.all()
    serializer_class = JogadorSerializer