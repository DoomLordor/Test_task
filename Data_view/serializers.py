from rest_framework import serializers

from .models import (Data, HeadByBK, TypeInstitutions,
                     TypeOrganizations, StatusEGRUL,
                     StatusRYBPNYBP, IndustrySpecificTyping)


class TypeInstitutionsSerializers(serializers.ModelSerializer):
    """Сериализатор типа учереждения"""

    class Meta:
        model = TypeInstitutions
        fields = '__all__'


class TypeOrganizationsSerializers(serializers.ModelSerializer):
    """Сериализатор типа учереждения"""

    class Meta:
        model = TypeOrganizations
        fields = '__all__'


class StatusEGRULSerializers(serializers.ModelSerializer):
    """Сериализатор статуса ЕГРУЛ"""

    class Meta:
        model = StatusEGRUL
        fields = '__all__'


class StatusRYBPNYBPSerializers(serializers.ModelSerializer):
    """Сериализатор статуса РУБПНУBП"""

    class Meta:
        model = StatusRYBPNYBP
        fields = '__all__'


class IndustrySpecificTypingSerializers(serializers.ModelSerializer):
    """Сериализатор отраслевая типизации"""

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

    type_institutions = TypeInstitutionsSerializers()

    type_organizations = TypeOrganizationsSerializers()

    status_egrul = StatusEGRULSerializers()

    status_rybpnybp = StatusRYBPNYBPSerializers()

    industry_specific_typing = IndustrySpecificTypingSerializers()

    head_by_bk = HeadByBKSerializers()

    class Meta:
        model = Data
        fields = '__all__'




