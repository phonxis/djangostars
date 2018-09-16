# Generated by Django 2.1.1 on 2018-09-16 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('modified_dt', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=128, verbose_name='First name')),
                ('last_name', models.CharField(max_length=128, verbose_name='Last name')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
        ),
    ]
