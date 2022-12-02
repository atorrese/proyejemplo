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


class Autor(models.Model):
    nombres = models.CharField(max_length=80, verbose_name=u'Nombres')
    apellido1 = models.CharField(max_length=80, verbose_name=u'Apellido Paterno')
    apellido2 = models.CharField(max_length=80, verbose_name=u'Apellido Materno')
    fechanacimiento = models.DateField(verbose_name=u'Fecha Nacimiento')
    genero = models.IntegerField(verbose_name=u'Genero', choices=GENEROS)

    def __str__(self):
        return u"%s %s %s" % (self.nombres, self.apellido1, self.apellido2)

    class Meta:
        verbose_name = u"Autor"
        verbose_name_plural = u"Autores"


class Libro(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    autores = models.ManyToManyField(Autor, blank=True)
    titulo = models.CharField(max_length=150, verbose_name=u'Titulo')
    prologo = models.TextField(verbose_name=u'Titulo')
    archivo = models.FileField(verbose_name=u'Archivo')

    def __str__(self):
        return u"%s" % self.titulo

    class Meta:
        verbose_name = u"Libro"
        verbose_name_plural = u"Libros"


