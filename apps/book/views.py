from rest_framework import authentication, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from ..rent.models import Rent
from ..rent.serializers import RentSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Author to be viewed or edited.
    """

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Book to be viewed or edited.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(
        methods=["post"],
        detail=True,
        authentication_classes=[authentication.TokenAuthentication],
        url_path="rent",
        url_name="rent-book",
        name="Rent",
    )
    def rent(self, request):
        """
        Rent a boook and return RentSerializer.
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
