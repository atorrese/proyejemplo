from rest_framework import viewsets

from api.serializers.auth.group import GroupSerializer
from django.contrib.auth.models import Group


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    #permission_classes = [permissions.IsAuthenticated]