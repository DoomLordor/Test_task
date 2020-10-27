from rest_framework import serializers

from .models import Data, HeadByBK


class HeadByBKSerializers(serializers.ModelSerializer):
    """Коды по бк"""
    class Meta:
        model = HeadByBK
        fields = '__all__'


class DataSerializers(serializers.ModelSerializer):
    """Обзор данных"""
    id_head_by_bk = HeadByBKSerializers()

    class Meta:
        model = Data
        fields = '__all__'




