from django.db import models

from common.models import BaseDates


class Author(BaseDates):
    first_name = models.CharField(
        "First name",
        max_length=128
    )
    last_name = models.CharField(
        "Last name",
        max_length=128
    )

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return "%s %s." % (self.last_name, self.first_name[0].upper())
