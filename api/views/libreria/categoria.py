from rest_framework import viewsets

from api.serializers.libreria.categoria import CategoriaSerializer
from apps.libreria.models import Categoria


class CatergoriaViewSet(viewsets.ModelViewSet):

    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
