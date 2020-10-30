from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from .models import Data, HeadByBK
from .serializers import DataSerializers, HeadByBKSerializers


class DataRest(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializers
    pagination_class = PaginationData
    filter_backends = (DjangoFilterBackend,)
    filterset_class = DataFilter
    permission_classes = (DataPermissions, )


class HeadByBKRest(viewsets.ModelViewSet):
    queryset = HeadByBK.objects.all()
    serializer_class = HeadByBKSerializers
    pagination_class = PaginationData
    filter_backends = (DjangoFilterBackend,)
    filterset_class = HeadByBKFilter
    permission_classes = (HeadByBKPermissions,)
