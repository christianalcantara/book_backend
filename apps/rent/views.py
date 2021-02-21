from .models import Rent

from .serializers import RentSerializer

from rest_framework import viewsets


class RentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Rent to be viewed or edited.
    """

    queryset = Rent.objects.all()
    serializer_class = RentSerializer
