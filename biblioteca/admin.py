from django.contrib import admin

# Register your models here.
from .models import Prestamo, Libro, Autor, Usuario

admin.site.register(Prestamo)
admin.site.register(Libro)
admin.site.register(Autor)
admin.site.register(Usuario)