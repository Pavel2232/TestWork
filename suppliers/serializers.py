from rest_framework import serializers

from suppliers.models import Suppliers


class SuppliersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suppliers
        fields = '__all__'
        read_only_fields = ['dept', ]
