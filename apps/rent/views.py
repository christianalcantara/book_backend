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
    def give_back(self, request):
        """
        Book rent give back
        is_admin user is required
        """
        book = self.get_object()
        user = request.user
        if user.is_authenticated:
            if book.is_available:
                rent = Rent.objects.create(user=user, book=book, price=book.price)
                rent_serializer = RentSerializer(rent, context={"request": request})
                return Response(status=status.HTTP_200_OK, data=rent_serializer.data)
            else:
                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    data={"detail": f"Book: '{book}' is not available for rent."},
                )
        return Response(status=status.HTTP_401_UNAUTHORIZED)
