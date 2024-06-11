from django.db import models


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

    def to_dict(self):
        return {
            'id': self.pk,
            'name': self.name,
            'edition': self.edition,
            'publication_year': self.publication_year,
            'authors': [author.name for author in self.authors.all()]
        }
