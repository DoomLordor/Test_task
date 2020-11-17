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
    """Коды по бк"""

    class Meta:
        model = HeadByBK
        fields = '__all__'


class CharacteristicsOrganizationSerializer(serializers.ModelSerializer):
    """Обзор данных"""

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

    def create1(self, validated_data):
        try:
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

            instance = CharacteristicsOrganization.objects.create(**validated_data)

            return instance
        except Exception:
            return

    # def update(self, instance, validated_data):
    #     validated_data['budget_level'] = validated_data['get_budget_level_display']
    #     validated_data.pop('get_budget_level_display')
    #
    #     for level in BudgetLevel.choices:
    #         if validated_data['budget_level'] in level:
    #             validated_data['budget_level'] = level[0]
    #
    #     for data in validated_data:
    #         if DataSerializers(instance).data[data] != validated_data[data]:
    #             instance.objects.update(**{data: validated_data[data]})
    #     return instance

