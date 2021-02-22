from rest_framework import serializers

from .models import Rent


class RentSerializer(serializers.HyperlinkedModelSerializer):
    fees = serializers.SerializerMethodField(read_only=True)
    rental_date = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S", read_only=True)
    return_date = serializers.DateTimeField(format="%d.%m.%Y %H:%M:%S", read_only=True)

    @staticmethod
    def get_fees(obj):
        return obj.fees_calculated

    class Meta:
        model = Rent
        fields = "__all__"
