from rest_framework import serializers

from .models import (Data, HeadByBK, TypeInstitutions,
                     TypeOrganizations, StatusEGRUL,
                     StatusRYBPNYBP, IndustrySpecificTyping)


class TypeInstitutionsSerializers(serializers.ModelSerializer):
    """Тип учереждения"""

    class Meta:
        model = TypeInstitutions
        fields = '__all__'


class TypeOrganizationsSerializers(serializers.ModelSerializer):
    """Тип учереждения"""

    class Meta:
        model = TypeOrganizations
        fields = '__all__'


class StatusEGRULSerializers(serializers.ModelSerializer):
    """Статус ЕГРУЛ"""

    class Meta:
        model = StatusEGRUL
        fields = '__all__'


class StatusRYBPNYBPSerializers(serializers.ModelSerializer):
    """Статус РУБПНУBП"""

    class Meta:
        model = StatusRYBPNYBP
        fields = '__all__'


class IndustrySpecificTypingSerializers(serializers.ModelSerializer):
    """Отраслевая типизация"""

    class Meta:
        model = IndustrySpecificTyping
        fields = '__all__'


class HeadByBKSerializers(serializers.ModelSerializer):
    """Коды по бк"""

    class Meta:
        model = HeadByBK
        fields = '__all__'


class DataSerializers(serializers.ModelSerializer):
    """Обзор данных"""

    type_institutions = serializers.SlugRelatedField(slug_field='type_institutions',
                                                        queryset=TypeInstitutions.objects.all())

    type_organizations = serializers.SlugRelatedField(slug_field='type_organizations',
                                                         queryset=TypeOrganizations.objects.all())

    status_egrul = serializers.SlugRelatedField(slug_field='status_egrul', queryset=StatusEGRUL.objects.all())

    status_rybpnybp = serializers.SlugRelatedField(slug_field='status_rybpnybp',
                                                      queryset=StatusRYBPNYBP.objects.all())

    industry_specific_typing = serializers.SlugRelatedField(slug_field='industry_specific_typing',
                                                               queryset=IndustrySpecificTyping.objects.all())

    head_by_bk = serializers.SlugRelatedField(slug_field='name_head_by_bk', queryset=HeadByBK.objects.all())

    class Meta:
        model = Data
        fields = '__all__'




