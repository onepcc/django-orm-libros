from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('autores', views.index2),
    path('procesar_libro', views.procesar_libro),
    path('procesar_autor', views.procesar_autor),
    path('procesar_autor_libro', views.procesar_autor_libro),
    path('procesar_libro_autor', views.procesar_libro_autor),
    path('ver_libro/<int:val>', views.ver_libro),
    path('ver_autor/<int:val>', views.ver_autor)
]
