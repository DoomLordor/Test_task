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

            massage = check_code(self.validated_data['code_head_by_bk'], 9)
            if massage:
                self._errors = {'code_head_by_bk': massage}
                return False

            return True
        else:
            return False


class AdvancedCharacteristicsOrganizationSerializer(serializers.ModelSerializer):
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

            massage = check_code(self.validated_data['inn'], 10)

            if massage:
                self._errors = {'inn': massage}
                return False

            massage = check_code(self.validated_data['kpp'], 9)

            if massage:
                self._errors = {'kpp': massage}
                return False

            return True
        else:
            return False


class CharacteristicsOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacteristicsOrganization
        fields = '__all__'


def check_code(code, len_code):
    """Проверка на соответствие кода указанной длине и состоит ли код из цифр"""
    if type(code) is not str:
        raise TypeError('code is not string')
    if type(len_code) is not int:
        raise TypeError('len_code is not integer')

    if len(code) != len_code:
        return 'Не верная длина'
    elif not code.isdigit():
        return 'Состоит не из цифр'
    return ''
