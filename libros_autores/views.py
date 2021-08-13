from django.shortcuts import render, HttpResponse, redirect
from time import  localtime, strftime
from libros_autores.models import *


def index(request):
    Libros=Book.objects.all() # se lee datos de la DB
    Autores=Publisher.objects.all() # se lee datos de la DB
    context = {
        'saludo': 'Libros y Autores',
        'book': Libros,
        'pub': Autores
    }

    return render(request, 'index.html', context)

def index2(request):
    Libros=Book.objects.all() # se lee datos de la DB
    Autores=Publisher.objects.all() # se lee datos de la DB
    context = {
        'saludo': 'Libros y Autores',
        'book': Libros,
        'pub': Autores
    }

    return render(request, 'index2.html', context)

def procesar_libro(request): # se crea vista que procesa el action del form en la plantilla
    if request.method == 'POST':
        print(request.POST)

        # leemos las variables del formulario

        titulo_libro= request.POST['titulo_libro']
        desc_libro= request.POST['descripcion_libro']
        
        
        # ejecutamos comando ORM para crear usauario, los campos deben coincidir con el modelo definido
        libro_db = Book.objects.create(
            titulo = titulo_libro,
            desc= desc_libro,
            )
        
        print("LIBRO CREADO CORRECTAMENTEE!!!", libro_db)
        
    return redirect('/')



def procesar_autor(request): # se crea vista que procesa el action del form en la plantilla
    if request.method == 'POST':
        print(request.POST)

        # leemos las variables del formulario
    
        nombre_autor= request.POST['nombre_autor']
        apellido_autor= request.POST['apellido_autor']
        notas_autor= request.POST['notas_autor']

        # ejecutamos comando ORM para crear usauario, los campos deben coincidir con el modelo definido
        
        autor_db = Publisher.objects.create(
            nombre = nombre_autor,
            apellido = apellido_autor,
            notas = notas_autor,
            )
        
        print("AUTOR CREADO CORRECTAMENTEE!!!", autor_db)

    return redirect('/autores')

def procesar_autor_libro(request): # se crea vista que procesa el action del form en la plantilla
    if request.method == 'POST':
        print(request.POST)

        # leemos las variables del formulario
    
        id_autor_libro= request.POST['id_autor_libro']
        libro_id= request.POST['libro_id']
        # ejecutamos comando ORM para crear usauario, los campos deben coincidir con el modelo definido
        
        autor_añadir= Publisher.objects.get(id=id_autor_libro)
        libro_mod= Book.objects.get(id=libro_id)


        lm=libro_mod.publishers.add(autor_añadir)

        
        print("AUTOR AÑADIDO CORRECTAMENTEE!!!", lm)

    return redirect(f'/ver_libro/{libro_id}')

def procesar_libro_autor(request): # se crea vista que procesa el action del form en la plantilla
    if request.method == 'POST':
        print(request.POST)

        # leemos las variables del formulario
    
        id_libro_autor= request.POST['id_libro_autor']
        autor_id= request.POST['autor_id']
        # ejecutamos comando ORM para crear usauario, los campos deben coincidir con el modelo definido
        
        libro_añadir= Book.objects.get(id=id_libro_autor)
        autor_mod= Publisher.objects.get(id=autor_id)


        am=autor_mod.books.add(libro_añadir)

        
        print("LIBRO AÑADIDO CORRECTAMENTEE!!!", am)

    return redirect(f'/ver_autor/{autor_id}')



def ver_libro(request, val):
    print(request)
    print("Libro a ver",val)
    libro_info = Book.objects.get(id=val) #informacion del libro con id = val
    
    all_autores = Publisher.objects.all() #informacion de todos los autores
    autores_libro=libro_info.publishers.all() #informacion autores del libro con id = val

    

    contexto ={
        'info_libro':libro_info,
        'todos_autores': all_autores,
        'autores_libro': autores_libro
        
    }
    
    
    return render(request, 'info_libro.html', contexto)

def ver_autor(request, val):
    print(request)
    print("Autor a ver",val)
    autor_info = Publisher.objects.get(id=val)
    
    all_books= Book.objects.all()
    libros_autor = autor_info.books.all()

    contexto ={
        'info_autor':autor_info,
        'todos_libros':all_books,
        'libros_autor':libros_autor 
    }
    
    
    return render(request, 'info_autor.html', contexto)
   