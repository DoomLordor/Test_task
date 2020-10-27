from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework as filters

from .models import Data, HeadByBK


comparison = {'GET': 'view', 'POST': 'add', 'PUT': 'change', 'PATCH': 'CHANGE', 'DELETE': 'delete', 'OPTIONS': 'view',
              'HEAD': 'view'}


class PaginationData(PageNumberPagination):
    page_size = 10


class DataFilter(filters.FilterSet):
    """Фильтры для обзорных данных"""
    budget_level = filters.CharFilter(lookup_expr='icontains')
    id_institutions = filters.NumberFilter()
    name_institutions = filters.CharFilter(lookup_expr='icontains')
    inn = filters.CharFilter(lookup_expr='icontains')
    kpp = filters.CharFilter(lookup_expr='icontains')
    type_institutions = filters.CharFilter(lookup_expr='icontains')
    type_organizations = filters.CharFilter(lookup_expr='icontains')
    status_egrul = filters.CharFilter(lookup_expr='icontains')
    status_rybpnybp = filters.CharFilter(lookup_expr='icontains')
    industry_specific_typing = filters.CharFilter(lookup_expr='icontains')
    id_head_by_bk = filters.CharFilter(field_name='id_head_by_bk__code_head_by_bk', lookup_expr='icontains')

    class Meta:
        model = Data
        fields = '__all__'


class HeadByBKFilter(filters.FilterSet):
    """Фильтры для кодов по БК"""
    class Meta:
        model = HeadByBK
        fields = '__all__'


class DataPermissions(permissions.BasePermission):
    """Проверка прав пользователя для обзорных данных"""
    def has_permission(self, request, view):
        return request.user.has_perm(f"Data_view.{comparison.get(request.method)}_data")


class HeadByBKPermissions(permissions.BasePermission):
    """Проверка прав пользователя для кодов по бк"""

    def has_permission(self, request, view):
        return request.user.has_perm(f"Data_view.{comparison.get(request.method)}_headbybk")




