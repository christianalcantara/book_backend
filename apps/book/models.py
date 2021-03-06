from django.db import models
from django.utils.translation import gettext_lazy as _


class Author(models.Model):
    """
    Author object
    """

    name = models.CharField(verbose_name=_("Name"), max_length=50)
    created = models.DateTimeField(
        verbose_name=_("Created"), editable=False, blank=True, auto_now_add=True
    )
    modified = models.DateTimeField(
        verbose_name=_("Modified"), editable=False, blank=True, auto_now=True
    )

    class Meta:
        ordering = ["name"]
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book object
    """

    title = models.CharField(verbose_name=_("Title"), max_length=150, db_index=True)
    description = models.TextField(verbose_name=_("description"))
    authors = models.ManyToManyField(
        verbose_name=_("Authors"), to=Author, related_name="books"
    )
    created = models.DateTimeField(
        verbose_name=_("Created"), editable=False, blank=True, auto_now_add=True
    )
    modified = models.DateTimeField(
        verbose_name=_("Modified"), editable=False, blank=True, auto_now=True
    )
    price = models.DecimalField(
        verbose_name=_("Rental price"),
        max_digits=9,
        decimal_places=2,
    )

    class Meta:
        ordering = ["-created", "title"]
        verbose_name = _("Book")
        verbose_name_plural = _("Books")

    def __str__(self):
        return self.title

    @property
    def is_available(self):
        """"check if the book is available"""
        return False if self.rents.filter(return_date__isnull=True).exists() else True
