import io
from django.core.management import call_command
from work_at_olist.base.models import Author


def test_authors_saved(db):
    """
    Certifies that the command created is saving the new
    authors to database and returning the correct message.
    """
    out = io.StringIO()
    call_command('import_authors', 'test_authors.csv', stdout=out)
    with open('test_authors.csv', 'r') as authors:
        a = [author for author in authors if author != 'name\n']
        for author_name in a:
            assert Author.objects.filter(name=author_name.rstrip('\n')).exists()
    assert f'{len(a)} authors created.' in out.getvalue()
    out.close()
