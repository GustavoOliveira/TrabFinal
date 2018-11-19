from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Organizador
from .serialize import OrganizadorSerializer
from rest_framework.permissions import IsAuthenticated

class OrganizadorList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Organizador.objects.all()
    serializer_class = OrganizadorSerializer


class OrganizadorDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = Organizador.objects.all()
    serializer_class = OrganizadorSerializer