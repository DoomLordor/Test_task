from rest_framework.response import Response
from rest_framework import viewsets, permissions, status, serializers
from rest_framework.pagination import PageNumberPagination

from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend

import characteristics_organizations.serializers as sr

from .models import (CharacteristicsOrganization, HeadByBK, TypeInstitution,
                     TypeOrganization, StatusEGRUL,
                     StatusRYBPNYBP, IndustrySpecificTyping)

COMPARISON = {'GET': 'view', 'POST': 'add', 'PUT': 'change', 'PATCH': 'CHANGE', 'DELETE': 'delete', 'OPTIONS': 'view',
              'HEAD': 'view'}


class PaginationData(PageNumberPagination):
    page_size = 10


# filters
class CharacteristicsOrganizationFilter(filters.FilterSet):
    """Фильтр для обзорных данных"""

    id_institutions = filters.NumberFilter()
    name_institutions = filters.CharFilter(lookup_expr='icontains')
    inn = filters.CharFilter(lookup_expr='icontains')
    kpp = filters.CharFilter(lookup_expr='icontains')
    type_institutions = filters.NumberFilter()
    type_organizations = filters.NumberFilter()
    status_egrul = filters.NumberFilter()
    status_rybpnybp = filters.NumberFilter()
    industry_specific_typing = filters.NumberFilter()
    head_by_bk = filters.CharFilter(field_name='head_by_bk__code_head_by_bk', lookup_expr='icontains')
    budget_level = filters.NumberFilter()

    class Meta:
        model = CharacteristicsOrganization
        fields = '__all__'


class HeadByBKFilter(filters.FilterSet):
    """Фильтр для кодов по БК"""

    class Meta:
        model = HeadByBK
        fields = '__all__'


class TypeInstitutionFilter(filters.FilterSet):
    """Фильтр для типов учреждений"""

    class Meta:
        model = TypeInstitution
        fields = '__all__'


class TypeOrganizationFilter(filters.FilterSet):
    """Фильтр для типов организаций"""

    class Meta:
        model = TypeOrganization
        fields = '__all__'


class StatusEGRULFilter(filters.FilterSet):
    """Фильтр для статусов ЕГРЮЛ"""

    class Meta:
        model = StatusEGRUL
        fields = '__all__'


class StatusRYBPNYBPFilter(filters.FilterSet):
    """Фильтр для статусов РУБПНУБП"""

    class Meta:
        model = StatusRYBPNYBP
        fields = '__all__'


class IndustrySpecificTypingFilter(filters.FilterSet):
    """Фильтр для отраслевой типизации"""

    class Meta:
        model = IndustrySpecificTyping
        fields = '__all__'


# filters

# Permissions
class CharacteristicsOrganizationPermission(permissions.BasePermission):
    """Проверка прав пользователя на работу с таблицей характеристик учреждений"""

    def has_permission(self, request, view):
        list_table_names = ['characteristicsorganization', 'headbybk', 'typeinstitutions', 'typeorganizations',
                            'statusegrul', 'statusrybpnybp', 'industryspecifictyping']
        if COMPARISON.get(request.method) == 'view':
            for table_name in list_table_names:
                if not request.user.has_perm(f"characteristics_organizations.view_{table_name}"):
                    return False
            return True

        return request.user.has_perm(f"characteristics_organizations.{COMPARISON.get(request.method)}_"
                                     f"characteristicsorganization")


class HeadByBKPermission(permissions.BasePermission):
    """Проверка прав пользователя на работу с таблицей кодов по БК"""

    def has_permission(self, request, view):
        return request.user.has_perm(f"characteristics_organizations.{COMPARISON.get(request.method)}_headbybk")


class TypeInstitutionPermission(permissions.BasePermission):
    """Проверка прав пользователя на работу с таблицей типов учреждений"""

    def has_permission(self, request, view):
        return request.user.has_perm(f"characteristics_organizations.{COMPARISON.get(request.method)}_typeinstitutions")


class TypeOrganizationPermission(permissions.BasePermission):
    """Проверка прав пользователя на работу с таблицей типов организаций"""

    def has_permission(self, request, view):
        return request.user.has_perm(f"characteristics_organizations.{COMPARISON.get(request.method)}_"
                                     f"typeorganizations")


class StatusEGRULPermission(permissions.BasePermission):
    """Проверка прав пользователя на работу с таблицей  статусов ЕГРЮЛ"""

    def has_permission(self, request, view):
        return request.user.has_perm(f"characteristics_organizations.{COMPARISON.get(request.method)}_statusegrul")


class StatusRYBPNYBPPermission(permissions.BasePermission):
    """Проверка прав пользователя на работу с таблицей статусов РУБПНУБП"""

    def has_permission(self, request, view):
        return request.user.has_perm(f"characteristics_organizations.{COMPARISON.get(request.method)}_statusrybpnybp")


class IndustrySpecificTypingPermission(permissions.BasePermission):
    """Проверка прав пользователя на работу с таблицей отраслевых типизаций"""

    def has_permission(self, request, view):
        return request.user.has_perm(f"characteristics_organizations.{COMPARISON.get(request.method)}_"
                                     f"industryspecifictyping")


# Permissions

# REST
class ModifiedModelViewSet(viewsets.ModelViewSet):

    def list(self, request, *args, **kwargs):
        if request.GET.get('paginate') is not None:
            self.pagination_class.page_size = request.GET.get('paginate')
            response = super().list(request, *args, **kwargs)
            self.pagination_class.page_size = 10
            return response
        else:
            return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return super().create(request, *args, **kwargs)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)

        if serializer.is_valid(raise_exception=True):
            return super().update(request, *args, **kwargs)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CharacteristicsOrganizationRest(ModifiedModelViewSet):
    queryset = CharacteristicsOrganization.objects.all()
    serializer_class = sr.CharacteristicsOrganizationSerializer
    pagination_class = PaginationData
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CharacteristicsOrganizationFilter
    permission_classes = (CharacteristicsOrganizationPermission,)

    def get_serializer_class(self):
        if self.action != 'list':
            return self.serializer_class
        return sr.AdvancedCharacteristicsOrganizationSerializer


class HeadByBKRest(ModifiedModelViewSet):
    queryset = HeadByBK.objects.all()
    serializer_class = sr.HeadByBKSerializer
    pagination_class = PaginationData
    filter_backends = (DjangoFilterBackend,)
    filterset_class = HeadByBKFilter
    permission_classes = (HeadByBKPermission,)


class TypeInstitutionRest(ModifiedModelViewSet):
    queryset = TypeInstitution.objects.all()
    serializer_class = sr.TypeInstitutionSerializer
    pagination_class = PaginationData
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TypeInstitutionFilter
    permission_classes = (HeadByBKPermission,)


class TypeOrganizationRest(ModifiedModelViewSet):
    queryset = TypeOrganization.objects.all()
    serializer_class = sr.TypeOrganizationSerializer
    pagination_class = PaginationData
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TypeOrganizationFilter
    permission_classes = (TypeOrganizationPermission,)


class StatusEGRULRest(ModifiedModelViewSet):
    queryset = StatusEGRUL.objects.all()
    serializer_class = sr.StatusEGRULSerializer
    pagination_class = PaginationData
    filter_backends = (DjangoFilterBackend,)
    filterset_class = StatusEGRULFilter
    permission_classes = (StatusEGRULPermission,)


class StatusRYBPNYBPRest(ModifiedModelViewSet):
    queryset = StatusRYBPNYBP.objects.all()
    serializer_class = sr.StatusRYBPNYBPSerializer
    pagination_class = PaginationData
    filter_backends = (DjangoFilterBackend,)
    filterset_class = StatusRYBPNYBPFilter
    permission_classes = (StatusRYBPNYBPPermission,)


class IndustrySpecificTypingRest(ModifiedModelViewSet):
    queryset = IndustrySpecificTyping.objects.all()
    serializer_class = sr.IndustrySpecificTypingSerializer
    pagination_class = PaginationData
    filter_backends = (DjangoFilterBackend,)
    filterset_class = IndustrySpecificTypingFilter
    permission_classes = (IndustrySpecificTypingPermission,)

# REST
