from django.urls import re_path, include

urlpatterns = [
    re_path(r'^auth/', include('api.views.auth.urls')),
    re_path(r'^libreria/', include('api.views.libreria.urls')),
]