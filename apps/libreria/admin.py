from django.contrib import admin
from apps.libreria.models import Categoria, Autor, Libro

admin.site.register(Categoria)
admin.site.register(Autor)
admin.site.register(Libro)
