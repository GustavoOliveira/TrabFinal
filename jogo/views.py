from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Jogo
from .serialize import JogoSerializer
from rest_framework.permissions import IsAuthenticated

class JogoList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer

class JogoDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer