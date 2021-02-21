from datetime import datetime
from decimal import Decimal

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from ..users.models import User


class Rent(models.Model):
    rental_date: datetime = models.DateTimeField(
        verbose_name=_("Rental date"), editable=False, blank=True, auto_now_add=True
    )
    return_date: datetime = models.DateTimeField(
        verbose_name=_("Return date"), blank=True, null=True
    )
    user: User = models.ForeignKey(
        verbose_name=_("User"), to=User, related_name="rents", on_delete=models.PROTECT
    )
    book = models.ForeignKey(
        verbose_name=_("Book"),
        to="book.Book",
        related_name="rents",
        on_delete=models.PROTECT,
    )
    late_fee_value: Decimal = models.DecimalField(
        verbose_name=_("late fee"),
        max_digits=9,
        decimal_places=2,
        blank=True,
        null=True,
    )
    interest_value: Decimal = models.DecimalField(
        verbose_name=_("Interest"),
        max_digits=9,
        decimal_places=2,
        blank=True,
        null=True,
    )
    amount: Decimal = models.DecimalField(
        verbose_name=_("Amount value"),
        max_digits=9,
        decimal_places=2,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("Rent")
        verbose_name_plural = _("Rents")
        ordering = ['-rental_date']

    def __str__(self):
        return f"{self.book.title}"

    @property
    def get_days(self):
        """ days from the rental date """
        now = timezone.now()
        return (now - self.rental_date).days

    @property
    def fees_calculated(self):
        """
        Ao retornar os livros emprestados, verificar de acordo com a regra sobre dias de atraso:
        Dias em atraso Multa Juros ao Dia
        Sem atraso        0%           0%
        Até 3 dias        3%         0.2%
        Acima 3 dias      5%         0.4%
        Acima 5 dias      7%         0.6%
        """
        book_price = self.book.price
        days = self.get_days
        amount = book_price
        if days == 3:
            late_fee = Decimal(3)
            interest = Decimal(0.2)
        elif days > 3:
            late_fee = Decimal(5)
            interest = Decimal(0.4)
        elif days > 5:
            late_fee = Decimal(7)
            interest = Decimal(0.6)
        else:
            late_fee = Decimal(0)
            interest = Decimal(0)
        late_fee_amount = book_price * late_fee / 100
        interest_amount = (book_price * interest / 100) * days
        amount = sum([book_price, late_fee_amount, interest_amount])
        return dict(
            days=days,
            book_price=book_price,
            amount=amount,
            late_fee=late_fee_amount,
            interest=interest_amount,
        )
