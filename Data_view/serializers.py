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

    def create(self, validated_data):
        validated_data['budget_level'] = validated_data['get_budget_level_display']
        validated_data.pop('get_budget_level_display')

        for level in BudgetLevel.choices:
            if validated_data['budget_level'] in level:
                validated_data['budget_level'] = level[0]

        validated_data['type_institutions'] = TypeInstitutions.objects.get_or_create(
            name_type=validated_data['type_institutions']['name_type'])[0]

        validated_data['type_organizations'] = TypeOrganizations.objects.get_or_create(
            name_type=validated_data['type_organizations']['name_type'])[0]

        validated_data['status_egrul'] = StatusEGRUL.objects.get_or_create(
            name_status=validated_data['status_egrul']['name_status'])[0]

        validated_data['status_rybpnybp'] = StatusRYBPNYBP.objects.get_or_create(
            name_status=validated_data['status_rybpnybp']['name_status'])[0]

        validated_data['industry_specific_typing'] = IndustrySpecificTyping.objects.get_or_create(
            name_typing=validated_data['industry_specific_typing']['name_typing'])[0]

        validated_data['head_by_bk'] = HeadByBK.objects.get_or_create(
            name_head_by_bk=validated_data['head_by_bk']['name_head_by_bk'],
            code_head_by_bk=validated_data['head_by_bk']['code_head_by_bk'])[0]

        data = Data.objects.create(**validated_data)

        return data


