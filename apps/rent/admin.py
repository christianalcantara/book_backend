from django.contrib import admin

from .models import Rent


@admin.register(Rent)
class RentAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "book",
        "rental_date",
        "return_date",
        "late_fee_value",
        "interest_value",
        "amount",
    )
    list_filter = ("rental_date", "return_date", "user", "book")
