
from django.urls import path,include

from api.views.libreria.categoria import CatergoriaViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'categorias', CatergoriaViewSet)

urlpatterns = [
    path('', include(router.urls), name='api_view_categoria'),
]