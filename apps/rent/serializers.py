from rest_framework import serializers

from .models import Rent


class RentSerializer(serializers.HyperlinkedModelSerializer):
    rent_value = serializers.SerializerMethodField(read_only=True)
    rental_date = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S", read_only=True)
    return_date = serializers.DateTimeField(format="%d.%m.%Y %H:%M:%S", read_only=True)

    @staticmethod
    def get_rent_value(obj):
        return obj.book.price

    class Meta:
        model = Rent
        fields = "__all__"
