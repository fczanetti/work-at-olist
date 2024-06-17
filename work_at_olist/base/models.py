from django.db import models
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            "id": self.pk,
            "name": self.name
        }


class Book(models.Model):
    name = models.CharField(max_length=64)
    edition = models.PositiveSmallIntegerField()
    publication_year = models.PositiveSmallIntegerField()
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('base:book_read', args=(self.pk,))

    def to_dict(self):
        return {
            'id': self.pk,
            'name': self.name,
            'edition': self.edition,
            'publication_year': self.publication_year,
            'authors': [author.pk for author in self.authors.all()]
        }
