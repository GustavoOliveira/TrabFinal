from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Campeonato
from .serialize import CampeonatoSerializer
from rest_framework.permissions import IsAuthenticated

class CampeonatoList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Campeonato.objects.all()
    serializer_class = CampeonatoSerializer

class CampeonatoDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = Campeonato.objects.all()
    serializer_class = CampeonatoSerializer