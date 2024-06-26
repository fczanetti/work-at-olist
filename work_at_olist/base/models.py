from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=64)
    edition = models.PositiveSmallIntegerField()
    publication_year = models.PositiveSmallIntegerField()
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/api/books/{self.pk}'
