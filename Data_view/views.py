from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination

from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import (DataSerializers, HeadByBKSerializers, TypeInstitutionsSerializers,
                          TypeOrganizationsSerializers, StatusEGRULSerializers,
                          StatusRYBPNYBPSerializers, IndustrySpecificTypingSerializers, BudgetLevelSerializers)
from .models import (Data, HeadByBK, TypeInstitutions,
                     TypeOrganizations, StatusEGRUL,
                     StatusRYBPNYBP, IndustrySpecificTyping, BudgetLevel)

comparison = {'GET': 'view', 'POST': 'add', 'PUT': 'change', 'PATCH': 'CHANGE', 'DELETE': 'delete', 'OPTIONS': 'view',
              'HEAD': 'view'}


class PaginationData(PageNumberPagination):
    page_size = 10


# filters
class DataFilter(filters.FilterSet):
    """Фильтры для обзорных данных"""

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
        model = Data
        fields = '__all__'


class HeadByBKFilter(filters.FilterSet):
    """Фильтры для кодов по БК"""

    class Meta:
        model = HeadByBK
        fields = '__all__'


class TypeInstitutionsFilter(filters.FilterSet):
    """Фильтры для типов учреждений"""

    class Meta:
        model = TypeInstitutions
        fields = '__all__'


class TypeOrganizationsFilter(filters.FilterSet):
    """Фильтры для типов организаций"""

    class Meta:
        model = TypeOrganizations
        fields = '__all__'


class StatusEGRULFilter(filters.FilterSet):
    """Фильтры для статусов ЕГРЮЛ"""

    class Meta:
        model = StatusEGRUL
        fields = '__all__'


class StatusRYBPNYBPFilter(filters.FilterSet):
    """Фильтры для статусов РУБПНУБП"""

    class Meta:
        model = StatusRYBPNYBP
        fields = '__all__'


class IndustrySpecificTypingFilter(filters.FilterSet):
    """Фильтры для отраслевой типизации"""

    class Meta:
        model = IndustrySpecificTyping
        fields = '__all__'


class BudgetLevelFilter(filters.FilterSet):
    """Фильтры для уровней бюджета"""

    class Meta:
        model = BudgetLevel
        fields = '__all__'


# filters

# Permissions
class DataPermissions(permissions.BasePermission):
    """Проверка прав пользователя для обзорных данных"""

    def has_permission(self, request, view):
        return request.user.has_perm(f"Data_view.{comparison.get(request.method)}_data")


class HeadByBKPermissions(permissions.BasePermission):
    """Проверка прав пользователя для кодов по бк"""

    def has_permission(self, request, view):
        return request.user.has_perm(f"Data_view.{comparison.get(request.method)}_headbybk")


class TypeInstitutionsPermissions(permissions.BasePermission):
    """Проверка прав пользователя для кодов по бк"""

    def has_permission(self, request, view):
        return request.user.has_perm(f"Data_view.{comparison.get(request.method)}_typeinstitutions")


class TypeOrganizationsPermissions(permissions.BasePermission):
    """Проверка прав пользователя для кодов по бк"""

    def has_permission(self, request, view):
        return request.user.has_perm(f"Data_view.{comparison.get(request.method)}_typeorganizations")


class StatusEGRULPermissions(permissions.BasePermission):
    """Проверка прав пользователя для кодов по бк"""

    def has_permission(self, request, view):
        return request.user.has_perm(f"Data_view.{comparison.get(request.method)}_statusegrul")


class StatusRYBPNYBPPermissions(permissions.BasePermission):
    """Проверка прав пользователя для кодов по бк"""

    def has_permission(self, request, view):
        return request.user.has_perm(f"Data_view.{comparison.get(request.method)}_status_rybpnybp")


class IndustrySpecificTypingPermissions(permissions.BasePermission):
    """Проверка прав пользователя для кодов по бк"""

    def has_permission(self, request, view):
        return request.user.has_perm(f"Data_view.{comparison.get(request.method)}_industryspecifictyping")


class BudgetLevelPermissions(permissions.BasePermission):
    """Проверка прав пользователя для кодов по бк"""

    def has_permission(self, request, view):
        return request.user.has_perm(f"Data_view.{comparison.get(request.method)}_budgetlevel")


# Permissions

# REST
class DataRest(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializers
    pagination_class = PaginationData
    filter_backends = (DjangoFilterBackend,)
    filterset_class = DataFilter
    permission_classes = (DataPermissions,)


class HeadByBKRest(viewsets.ModelViewSet):
    queryset = HeadByBK.objects.all()
    serializer_class = HeadByBKSerializers
    pagination_class = PaginationData
    filter_backends = (DjangoFilterBackend,)
    filterset_class = HeadByBKFilter
    permission_classes = (HeadByBKPermissions,)


class TypeInstitutionsRest(viewsets.ModelViewSet):
    queryset = TypeInstitutions.objects.all()
    serializer_class = TypeInstitutionsSerializers
    pagination_class = PaginationData
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TypeInstitutionsFilter
    permission_classes = (HeadByBKPermissions,)


class TypeOrganizationsRest(viewsets.ModelViewSet):
    queryset = TypeOrganizations.objects.all()
    serializer_class = TypeOrganizationsSerializers
    pagination_class = PaginationData
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TypeOrganizationsFilter
    permission_classes = (TypeOrganizationsPermissions,)


class StatusEGRULRest(viewsets.ModelViewSet):
    queryset = StatusEGRUL.objects.all()
    serializer_class = StatusEGRULSerializers
    pagination_class = PaginationData
    filter_backends = (DjangoFilterBackend,)
    filterset_class = StatusEGRULFilter
    permission_classes = (StatusEGRULPermissions,)


class StatusRYBPNYBPRest(viewsets.ModelViewSet):
    queryset = StatusRYBPNYBP.objects.all()
    serializer_class = StatusRYBPNYBPSerializers
    pagination_class = PaginationData
    filter_backends = (DjangoFilterBackend,)
    filterset_class = StatusRYBPNYBPFilter
    permission_classes = (StatusRYBPNYBPPermissions,)


class IndustrySpecificTypingRest(viewsets.ModelViewSet):
    queryset = IndustrySpecificTyping.objects.all()
    serializer_class = IndustrySpecificTypingSerializers
    pagination_class = PaginationData
    filter_backends = (DjangoFilterBackend,)
    filterset_class = IndustrySpecificTypingFilter
    permission_classes = (IndustrySpecificTypingPermissions,)


class BudgetLevelRest(viewsets.ModelViewSet):
    queryset = BudgetLevel.objects.all()
    serializer_class = BudgetLevelSerializers
    pagination_class = PaginationData
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BudgetLevelFilter
    permission_classes = (BudgetLevelPermissions,)

# REST
