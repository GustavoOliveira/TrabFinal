from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Clube
from .serialize import ClubeSerializer
from rest_framework.permissions import IsAuthenticated

class ClubeList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Clube.objects.all()
    serializer_class = ClubeSerializer

class ClubeDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = Clube.objects.all()
    serializer_class = ClubeSerializer