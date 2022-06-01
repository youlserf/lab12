from rest_framework import serializers

from .models import Prestamo, Libro, Usuario

class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = ['id', 'usuario', 'libro', 'f_prestamo', 'f_devolucion']
""" 
class InnerJoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = ['id', 'usuario', 'libro', 'f_prestamo', 'f_devolucion', ""]
        
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ['codigo', 'titulo']
        
class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nombre'] """