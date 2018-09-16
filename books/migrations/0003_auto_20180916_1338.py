# Generated by Django 2.1.1 on 2018-09-16 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_publish_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(help_text='International Standard Book Number', max_length=13, verbose_name='ISBN'),
        ),
    ]