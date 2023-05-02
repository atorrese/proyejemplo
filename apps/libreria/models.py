from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=150, verbose_name=u'Nombre')

    def __str__(self):
        return u"%s" % self.nombre

    class Meta:
        verbose_name = u"Categoria"
        verbose_name_plural = u"Categorias"


GENEROS = (
    (0, 'Sin genero'),
    (1, 'Femenino'),
    (2, 'Masculino'),
)


class Autor(models.Model):#Nombre de clase en django y por defecto nombre de la tabla
    #Atributos
    nombres = models.CharField(max_length=80, verbose_name=u'Nombres')
    apellido1 = models.CharField(max_length=80, verbose_name=u'Apellido Paterno')
    apellido2 = models.CharField(max_length=80, verbose_name=u'Apellido Materno')
    fechanacimiento = models.DateField(verbose_name=u'Fecha Nacimiento')
    genero = models.IntegerField(verbose_name=u'Genero', choices=GENEROS)

    def __str__(self):# Metodo de presentación de cada registro o objecto
        return u"%s %s %s" % (self.nombres, self.apellido1, self.apellido2)

    class Meta:
        # Nombre en plural en sitio de administación django
        verbose_name = u"Autor"
        #Nombre en plural en sitio de administación django
        verbose_name_plural = u"Autores"
        #Nombre de tabla en sql server
        db_table = 'libreria_autor'


class Libro(models.Model):
    categoria = models.ForeignKey(to=Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    autores = models.ManyToManyField(Autor, blank=True)
    titulo = models.CharField(max_length=150, verbose_name=u'Titulo')
    prologo = models.TextField(verbose_name=u'Titulo')
    archivo = models.FileField(verbose_name=u'Archivo')

    def __str__(self):
        return u"%s" % self.titulo

    class Meta:
        verbose_name = u"Libro"
        verbose_name_plural = u"Libros"


