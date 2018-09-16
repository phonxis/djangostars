from django.db import models

from authors.models import Author
from common.models import BaseDates


class Book(BaseDates):
    title = models.CharField(
        "Title",
        max_length=255
    )
    isbn = models.CharField(
        "ISBN",
        max_length=13,
        help_text="International Standard Book Number"
    )
    price = models.DecimalField(
        "Price",
        max_digits=10,
        decimal_places=2,
        default=0
    )
    authors = models.ManyToManyField(
        Author,
        related_name="books"
    )
    publish_date = models.DateField(
        "Publication date"
    )

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = ('-created_dt',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        if '-' in self.isbn:
            self.isbn = self.isbn.replace('-', '')

        super().save(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # set previous values
        for field in self.fields_for_logging():
            setattr(self, 'prev_%s' % field, getattr(self, field))

    def fields_for_logging(self):
        """
            Set which fields will be saved in log table
        """
        return ['title', 'isbn', 'price', 'publish_date']


class LogBookAction(BaseDates):
    CREATE = "create"
    DELETE = "delete"
    UPDATE = "update"

    ACTION_CHOICES = (
        (CREATE, "Create"),
        (DELETE, "Delete"),
        (UPDATE, "Update"),
    )

    # previuos values
    prev_title = models.TextField(
        "Previous title",
        blank=True
    )
    prev_isbn = models.TextField(
        "Previous ISBN",
        blank=True
    )
    prev_price = models.TextField(
        "Previous price",
        blank=True
    )
    prev_publish_date = models.TextField(
        "Previous publication date",
        blank=True
    )

    # current values
    title = models.TextField(
        "Current title",
        blank=True
    )
    isbn = models.TextField(
        "Current ISBN",
        blank=True
    )
    price = models.TextField(
        "Current price",
        blank=True
    )
    publish_date = models.TextField(
        "Current publication date",
        blank=True
    )

    user = models.TextField(
        "Who manipulate book",
        blank=True
    )
    action_type = models.CharField(
        "Action type",
        max_length=10,
        choices=ACTION_CHOICES,
        default=CREATE
    )

    class Meta:
        verbose_name = "Log book action"
        verbose_name_plural = "Log book actions"
        ordering = ('-created_dt',)

    def __str__(self):
        return self.action_type
