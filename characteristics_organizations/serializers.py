from rest_framework import serializers

from .models import (CharacteristicsOrganization, HeadByBK, TypeInstitution,
                     TypeOrganization, StatusEGRUL,
                     StatusRYBPNYBP, IndustrySpecificTyping, BudgetLevel)


class TypeInstitutionSerializer(serializers.ModelSerializer):
    """Сериализатор типа учереждения"""

    class Meta:
        model = TypeInstitution
        fields = '__all__'


class TypeOrganizationSerializer(serializers.ModelSerializer):
    """Сериализатор типа учереждения"""

    class Meta:
        model = TypeOrganization
        fields = '__all__'


class StatusEGRULSerializer(serializers.ModelSerializer):
    """Сериализатор статуса ЕГРУЛ"""

    class Meta:
        model = StatusEGRUL
        fields = '__all__'


class StatusRYBPNYBPSerializer(serializers.ModelSerializer):
    """Сериализатор статуса РУБПНУBП"""

    class Meta:
        model = StatusRYBPNYBP
        fields = '__all__'


class IndustrySpecificTypingSerializer(serializers.ModelSerializer):
    """Сериализатор отраслевая типизации"""

    class Meta:
        model = IndustrySpecificTyping
        fields = '__all__'


class HeadByBKSerializer(serializers.ModelSerializer):
    """Сериализатор кода по бк"""

    class Meta:
        model = HeadByBK
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        if super().is_valid(raise_exception):

            if not self.validated_data['code_head_by_bk'].isdigit():
                self._errors = {'code_head_by_bk': 'Код главы по БК сотстоит не из цифр'}
            elif not self._errors and len(self.validated_data['code_head_by_bk']) != 3:
                self._errors = {'code_head_by_bk': 'Код главы по БК не верной длины'}

            return not bool(self._errors)
        else:
            return False

class CharacteristicsOrganizationSerializerFromList(serializers.ModelSerializer):
    """Сериализатор характеристик организации"""

    budget_level = serializers.CharField(source='get_budget_level_display')

    type_institution = TypeInstitutionSerializer()

    type_organization = TypeOrganizationSerializer()

    status_egrul = StatusEGRULSerializer()

    status_rybpnybp = StatusRYBPNYBPSerializer()

    industry_specific_typing = IndustrySpecificTypingSerializer()

    head_by_bk = HeadByBKSerializer()

    class Meta:
        model = CharacteristicsOrganization
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        if super().is_valid(raise_exception):

            error = check_INN(self.validated_data['inn'])

            if error:
                self._errors = error
                return False

            error = check_KPP(self.validated_data['kpp'])

            if error:
                self._errors = error
                return False
        else:
            return False

class CharacteristicsOrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = CharacteristicsOrganization
        fields = '__all__'

def check_INN(INN):
    if len(INN) != 10:
        return {'inn': 'Не верная длина ИНН организации'}
    elif not INN.isdigit():
        return {'inn': 'ИНН состоит не из цифр'}
    return {}

def check_KPP(KPP):
    if len(KPP) != 10:
        return {'kpp': 'Не верная длина КПП организации'}
    elif not KPP.isdigit():
        return {'kpp': 'Кпп состоит не из цифр'}
    return {}
