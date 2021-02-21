from rest_framework import routers
from apps.users.views import UserViewSet, CustomerViewSet
from apps.book.views import AuthorViewSet, BookViewSet
from apps.rent.views import RentViewSet

# Settings
api = routers.DefaultRouter()
api.trailing_slash = "/?"

# Users API
api.register(r"users", viewset=UserViewSet)
api.register(r"customers", viewset=CustomerViewSet)

# Books API
api.register(r"autors", AuthorViewSet)
api.register(r"books", BookViewSet)

# Rent API

api.register(r"rent", RentViewSet)
