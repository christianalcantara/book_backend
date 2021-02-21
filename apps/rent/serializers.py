from rest_framework import serializers

from .models import Rent


class RentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rent
        fields = "__all__"
