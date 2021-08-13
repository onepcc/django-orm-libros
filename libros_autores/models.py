from django.db import models

# Create your models here.

class Book(models.Model):
    titulo = models.CharField(max_length=255)
    desc = models.TextField(default='vacio')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #publishers = autores del libro
    def __repr__(self):
            return f"<Titulo: {self.title}>"


class Publisher(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    notas = models.TextField(default='vacio')
    books = models.ManyToManyField(Book, related_name="publishers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #
    def __repr__(self):
            return f"<Nombre: {self.name} {self.books.name}, {self.updated_at}>"