from rest_framework import viewsets, mixins, status
from .serializers import *


class JovViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = JobSerializer
    queryset = serializer_class.Meta.model.objects.all()