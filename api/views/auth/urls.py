from django.urls import include, path
from rest_framework import routers
from api.views.auth import user, group

router = routers.DefaultRouter()
router.register(r'users', user.UserViewSet)
router.register(r'groups', group.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]