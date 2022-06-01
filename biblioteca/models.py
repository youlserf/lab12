from django.db import models



class Autor(models.Model):
    name = models.CharField(max_length=100)
    nation = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Libro(models.Model):
    autor =  models.ForeignKey(Autor, on_delete=models.CASCADE)
    codigo = models.IntegerField()
    titulo = models.CharField(max_length=100)
    isbn = models.CharField(max_length=30)
    editorial = models.CharField(max_length=60)
    num_pages = models.SmallIntegerField()
    def __str__(self):
        return self.titulo
# Cre your models here.

class Usuario(models.Model):
    user_name = models.CharField(max_length=50)
    dni = models.IntegerField()
    nombre  = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    telefono = models.IntegerField()
    def __str__(self):
        return self.user_name

class Prestamo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    f_prestamo = models.DateField()
    f_devolucion = models.DateField()
    def __str__(self):
        return self.usuario.user_name

