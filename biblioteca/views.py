from django.shortcuts import render
""" Usuario """
from rest_framework import viewsets

  
from .serializers import PrestamoSerializer
from .models import Prestamo, Libro, Usuario
# Create your views here.
class PrestamoViewSet(viewsets.ModelViewSet):

    queryset = Prestamo.objects.all().values_list("libro").union(Libro.objects.all().values_list("titulo"))
    serializer_class = PrestamoSerializer


 

