from django.shortcuts import render
""" Usuario """
from rest_framework import viewsets
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

  
from .serializers import PrestamoSerializer
from .models import Prestamo, Libro, Usuario
# Create your views here.
class PrestamoViewSet(viewsets.ModelViewSet):

    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer


 

