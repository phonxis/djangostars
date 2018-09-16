from django.core.management.base import BaseCommand

from books.models import Book


class Command(BaseCommand):
    help = "Display list of books with ordering ASC[default]/DESC"

    def add_arguments(self, parser):
        parser.add_argument(
            '-o', '--ordering', type=str, help='Ordering type (ASC/DESC)'
        )

    def handle(self, *args, **kwargs):
        ordering_dict = {
            "ASC": "publish_date",  # ASC
            "DESC": "-publish_date",  # DESC
            "DEFAULT": "publish_date"  # ASC
        }

        ordering = kwargs["ordering"] or "default"

        qs = Book.objects.all().order_by(ordering_dict[ordering.upper()])

        for book in qs:
            self.stdout.write(book.title)
