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


class CharacteristicsOrganizationSerializer(serializers.ModelSerializer):
    """Сериализатор характеристик организации"""

    budget_level = serializers.CharField(source='get_budget_level_display')

    type_institutions = TypeInstitutionSerializer()

    type_organizations = TypeOrganizationSerializer()

    status_egrul = StatusEGRULSerializer()

    status_rybpnybp = StatusRYBPNYBPSerializer()

    industry_specific_typing = IndustrySpecificTypingSerializer()

    head_by_bk = HeadByBKSerializer()

    class Meta:
        model = CharacteristicsOrganization
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        if super().is_valid(raise_exception):
            for level in BudgetLevel.choices:
                if self.validated_data['get_budget_level_display'] in level:
                    break
            else:
                self._errors = {'budget_level': 'Такой уровень бюджета отсутствует'}

            if not self._errors and not TypeInstitution.objects.filter(
                    name_type=self.validated_data['type_institutions']['name_type']).exists():
                self._errors = {'type_institutions': 'Данный тип учреждения отсутствует'}

            elif not self._errors and not TypeOrganization.objects.filter(
                    name_type=self.validated_data['type_organizations']['name_type']).exists():

                self._errors = {'type_organizations': 'Данный тип организации отсутствует'}

            elif not self._errors and not StatusEGRUL.objects.filter(
                    name_status=self.validated_data['status_egrul']['name_status']).exists():

                self._errors = {'status_egrul': 'Данный статус ЕГРЮЛ отсутствует'}

            elif not self._errors and not StatusRYBPNYBP.objects.filter(
                    name_status=self.validated_data['status_rybpnybp']['name_status']).exists():

                self._errors = {'status_rybpnybp': 'Данный статус РУБПНУБП отсутствует'}

            elif not self._errors and not IndustrySpecificTyping.objects.filter(
                    name_typing=self.validated_data['industry_specific_typing']['name_typing']).exists():

                self._errors = {'industry_specific_typing': 'Данная отраслевая типизация отсутствует'}

            elif not self._errors and not HeadByBK.objects.filter(
                    name_head_by_bk=self.validated_data['head_by_bk']['name_head_by_bk'],
                    code_head_by_bk=self.validated_data['head_by_bk']['code_head_by_bk']).exists():

                self._errors = {'head_by_bk': 'Данная глава по бк отсутствует'}

            elif not self._errors and len(self.validated_data['inn']) != 10:
                self._errors = {'inn': 'Не верная длина ИНН организации'}

            elif not self._errors and not self.validated_data['inn'].isdigit():
                self._errors = {'inn': 'ИНН не является числом'}

            elif not self._errors and len(self.validated_data['kpp']) != 9:
                self._errors = {'kpp': 'Не верная длина КПП организации'}

            elif not self._errors and not self.validated_data['kpp'].isdigit():
                self._errors = {'kpp': 'КПП не является числом'}

            return not bool(self._errors)

        else:
            return False

    def create(self, validated_data):
        return super().create(convert_validated_data(validated_data))

    def update(self, instance, validated_data):
        return super().update(instance, convert_validated_data(validated_data))


def convert_validated_data(validated_data):
    """Конвертация данных в объекты таблиц связных таблиц и преобразование метки в значение"""

    validated_data['budget_level'] = validated_data['get_budget_level_display']
    validated_data.pop('get_budget_level_display')

    for level in BudgetLevel.choices:
        if validated_data['budget_level'] in level:
            validated_data['budget_level'] = level[0]

    validated_data['type_institutions'] = TypeInstitution.objects.get(
        name_type=validated_data['type_institutions']['name_type'])

    validated_data['type_organizations'] = TypeOrganization.objects.get(
        name_type=validated_data['type_organizations']['name_type'])

    validated_data['status_egrul'] = StatusEGRUL.objects.get(
        name_status=validated_data['status_egrul']['name_status'])

    validated_data['status_rybpnybp'] = StatusRYBPNYBP.objects.get(
        name_status=validated_data['status_rybpnybp']['name_status'])

    validated_data['industry_specific_typing'] = IndustrySpecificTyping.objects.get(
        name_typing=validated_data['industry_specific_typing']['name_typing'])

    validated_data['head_by_bk'] = HeadByBK.objects.get(
        name_head_by_bk=validated_data['head_by_bk']['name_head_by_bk'],
        code_head_by_bk=validated_data['head_by_bk']['code_head_by_bk'])

    return validated_data
