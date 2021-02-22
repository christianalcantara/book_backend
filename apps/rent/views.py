from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rest_framework import authentication, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Rent
from .serializers import RentSerializer


class RentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Rent to be viewed or edited.
    """

    authentication_classes = [
        authentication.TokenAuthentication,
        authentication.SessionAuthentication,
    ]
    permission_classes = [permissions.IsAuthenticated]

    queryset = Rent.objects.all()
    serializer_class = RentSerializer

    def get_queryset(self):
        """ if the user is a customer returns only their rentals """
        user = self.request.user
        if user.is_customer:
            return Rent.objects.filter(user=user)
        return super().get_queryset()

    @action(
        methods=["post"],
        detail=True,
        authentication_classes=[authentication.TokenAuthentication],
        url_path="give-back",
        url_name="rent-give-back",
        name="Book give back",
    )
    def give_back(self, request, pk=None):
        """
        Book rent give back and update values from property function 'fess_calculated'
        admin user is required to receive
        """
        rent = self.get_object()
        user = request.user
        if user.is_authenticated and user.is_admin:
            if rent.return_date:
                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    data={"detail": _(f"This rent is closed.")},
                )
            else:
                fees = rent.fees_calculated
                rent.user = user
                rent.amount = fees.get("amount")
                rent.late_fee_value = fees.get("late_fee")
                rent.interest_value = fees.get("interest")
                rent.return_date = timezone.now()
                rent.save()
                rent_serializer = self.serializer_class(
                    rent, context={"request": request}
                )
                return Response(status=status.HTTP_200_OK, data=rent_serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
