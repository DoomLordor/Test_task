from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination

from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import (CharacteristicsOrganizationSerializer, HeadByBKSerializer, TypeInstitutionSerializer,
                          TypeOrganizationSerializer, StatusEGRULSerializer,
                          StatusRYBPNYBPSerializer, IndustrySpecificTypingSerializer)
from .models import (CharacteristicsOrganization, HeadByBK, TypeInstitution,
                     TypeOrganization, StatusEGRUL,
                     StatusRYBPNYBP, IndustrySpecificTyping)

COMPARISON = {'GET': 'view', 'POST': 'add', 'PUT': 'change', 'PATCH': 'CHANGE', 'DELETE': 'delete', 'OPTIONS': 'view',
              'HEAD': 'view'}


class PaginationData(PageNumberPagination):
    page_size = 10


# filters
class CharacteristicsOrganizationFilter(filters.FilterSet):
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
        model = CharacteristicsOrganization
        fields = '__all__'


class HeadByBKFilter(filters.FilterSet):
    """Фильтры для кодов по БК"""

    class Meta:
        model = HeadByBK
        fields = '__all__'


class TypeInstitutionFilter(filters.FilterSet):
    """Фильтры для типов учреждений"""

    class Meta:
        model = TypeInstitution
        fields = '__all__'


class TypeOrganizationFilter(filters.FilterSet):
    """Фильтры для типов организаций"""

    class Meta:
        model = TypeOrganization
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

# filters

# Permissions
class CharacteristicsOrganizationPermissions(permissions.BasePermission):
    """Проверка прав пользователя для обзорных данных"""

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


class HeadByBKPermissions(permissions.BasePermission):
    """Проверка прав пользователя для кодов по бк"""

    def has_permission(self, request, view):
        return request.user.has_perm(f"characteristics_organizations.{COMPARISON.get(request.method)}_headbybk")


class TypeInstitutionPermissions(permissions.BasePermission):
    """Проверка прав пользователя для кодов по бк"""

    def has_permission(self, request, view):
        return request.user.has_perm(f"characteristics_organizations.{COMPARISON.get(request.method)}_typeinstitutions")


class TypeOrganizationPermissions(permissions.BasePermission):
    """Проверка прав пользователя для кодов по бк"""

    def has_permission(self, request, view):
        return request.user.has_perm(f"characteristics_organizations.{COMPARISON.get(request.method)}_"
                                     f"typeorganizations")


class StatusEGRULPermissions(permissions.BasePermission):
    """Проверка прав пользователя для кодов по бк"""

    def has_permission(self, request, view):
        return request.user.has_perm(f"characteristics_organizations.{COMPARISON.get(request.method)}_statusegrul")


class StatusRYBPNYBPPermissions(permissions.BasePermission):
    """Проверка прав пользователя для кодов по бк"""

    def has_permission(self, request, view):
        return request.user.has_perm(f"characteristics_organizations.{COMPARISON.get(request.method)}_statusrybpnybp")


class IndustrySpecificTypingPermissions(permissions.BasePermission):
    """Проверка прав пользователя для кодов по бк"""

    def has_permission(self, request, view):
        return request.user.has_perm(f"characteristics_organizations.{COMPARISON.get(request.method)}_"
                                     f"industryspecifictyping")

# Permissions

# REST
class CharacteristicsOrganizationRest(viewsets.ModelViewSet):
    queryset = CharacteristicsOrganization.objects.all()
    serializer_class = CharacteristicsOrganizationSerializer
    pagination_class = PaginationData
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CharacteristicsOrganizationFilter
    permission_classes = (CharacteristicsOrganizationPermissions,)

    def list(self, request, *args, **kwargs):
        if request.GET.get('paginate') is not None:
            self.pagination_class.page_size = request.GET.get('paginate')
        return super().list(request, *args, **kwargs)



class HeadByBKRest(viewsets.ModelViewSet):
    queryset = HeadByBK.objects.all()
    serializer_class = HeadByBKSerializer
    pagination_class = PaginationData
    filter_backends = (DjangoFilterBackend,)
    filterset_class = HeadByBKFilter
    permission_classes = (HeadByBKPermissions,)


class TypeInstitutionRest(viewsets.ModelViewSet):
    queryset = TypeInstitution.objects.all()
    serializer_class = TypeInstitutionSerializer
    pagination_class = PaginationData
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TypeInstitutionFilter
    permission_classes = (HeadByBKPermissions,)


class TypeOrganizationRest(viewsets.ModelViewSet):
    queryset = TypeOrganization.objects.all()
    serializer_class = TypeOrganizationSerializer
    pagination_class = PaginationData
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TypeOrganizationFilter
    permission_classes = (TypeOrganizationPermissions,)


class StatusEGRULRest(viewsets.ModelViewSet):
    queryset = StatusEGRUL.objects.all()
    serializer_class = StatusEGRULSerializer
    pagination_class = PaginationData
    filter_backends = (DjangoFilterBackend,)
    filterset_class = StatusEGRULFilter
    permission_classes = (StatusEGRULPermissions,)


class StatusRYBPNYBPRest(viewsets.ModelViewSet):
    queryset = StatusRYBPNYBP.objects.all()
    serializer_class = StatusRYBPNYBPSerializer
    pagination_class = PaginationData
    filter_backends = (DjangoFilterBackend,)
    filterset_class = StatusRYBPNYBPFilter
    permission_classes = (StatusRYBPNYBPPermissions,)


class IndustrySpecificTypingRest(viewsets.ModelViewSet):
    queryset = IndustrySpecificTyping.objects.all()
    serializer_class = IndustrySpecificTypingSerializer
    pagination_class = PaginationData
    filter_backends = (DjangoFilterBackend,)
    filterset_class = IndustrySpecificTypingFilter
    permission_classes = (IndustrySpecificTypingPermissions,)

# REST
