from rest_framework import serializers

from .models import (Data, HeadByBK, TypeInstitutions,
                     TypeOrganizations, StatusEGRUL,
                     StatusRYBPNYBP, IndustrySpecificTyping, BudgetLevel)

bl = {0: 'Не определен',
      1: 'Федеральный бюджет',
      2: 'Бюджет муниципального района',
      3: 'Местный бюджет',
      4: 'Бюджет городского округа',
      5: 'Бюджет муниципального района',
      6: 'Бюджет городского поселения',
      7: 'Бюджет сельского поселения',
      8: 'Бюджет государственного внебюджетного фонда Российской Федерации',
      9: 'Бюджет Пенсионного фонда Российской Федерации',
      10: 'Бюджет Фонда социального страхования Российской Федерации',
      11: 'Бюджет Федерального фонда обязательного медицинского страхования',
      12: 'Бюджет территориального государственного внебюджетного фонда',
      13: 'Бюджет городского округа с внутригородским делением',
      14: 'Бюджет внутригородского муниципального'
          ' образования города федерального значения',
      15: 'Бюджет внутригородского района'}


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


class BudgetLevelSerializers(serializers.ModelSerializer):
    """Уровень бюджета"""

    class Meta:
        model = BudgetLevel
        fields = '__all__'


class HeadByBKSerializers(serializers.ModelSerializer):
    """Коды по бк"""

    class Meta:
        model = HeadByBK
        fields = '__all__'


class DataSerializers(serializers.ModelSerializer):
    """Обзор данных"""
    budget_level = serializers.SlugRelatedField(slug_field='budget_level', queryset=BudgetLevel.objects.all())

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




