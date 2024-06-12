import pytest
from work_at_olist.base.models import Author


@pytest.fixture
def author(db):
    """
    Creates and returns an author.
    """
    author = Author.objects.create(name='Author 01')
    return author
