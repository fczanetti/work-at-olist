[![codecov](https://codecov.io/gh/fczanetti/work-at-olist/graph/badge.svg?token=FW6xWklGdj)](https://codecov.io/gh/fczanetti/work-at-olist)
![CI](https://github.com/fczanetti/work-at-olist/actions/workflows/work_01.yml/badge.svg)

![Python](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Ffczanetti%2Fwork-at-olist%2Fmain%2FPipfile.lock&query=%24._meta.requires.python_version&label=Python&labelColor=%232b5b84&color=%233d3d3e)
![Django](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Ffczanetti%2Fwork-at-olist%2Fmain%2FPipfile.lock&query=%24%5B'default'%5D%5B'django'%5D%5B'version'%5D&label=Django&labelColor=%230c3c26&color=%233d3d3e)
![Django Ninja](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Ffczanetti%2Fwork-at-olist%2Fmain%2FPipfile.lock&query=%24%5B'default'%5D%5B'django-ninja'%5D%5B'version'%5D&label=Django%20Ninja&labelColor=%234cae4f&color=%233d3d3e)


# Work at Olist

Welcome to work-at-olist project documentation!

This project was developed to solve the challenge proposed by Olist. It consists of an API to store names of authors and books written by them. The requirements were to create a management command to import and save the names of the authors from a .csv file, and also a CRUD to manage the books. An important detail is that a book can be written by more than one author, so a many-to-many relations was used to create the database. Some filters were also created to retrieve books or authors, but these were optional.

More details can be checked in [their requirements](https://github.com/fczanetti/work-at-olist/blob/main/olist_instructions.md). You can also visit the [original repository](https://github.com/olist/work-at-olist).


# Content

- [Database](https://github.com/fczanetti/work-at-olist?tab=readme-ov-file#database)
- [Folder strucure](https://github.com/fczanetti/work-at-olist?tab=readme-ov-file#folder-structure)
- [Installing](https://github.com/fczanetti/work-at-olist?tab=readme-ov-file#installing)
- [Installing with Docker](https://github.com/fczanetti/work-at-olist?tab=readme-ov-file#installing-with-docker)
- [Importing authors from .csv](https://github.com/fczanetti/work-at-olist?tab=readme-ov-file#importing-authors-from-csv)
- [Running tests](https://github.com/fczanetti/work-at-olist?tab=readme-ov-file#running-tests)
- [API documentation](https://github.com/fczanetti/work-at-olist?tab=readme-ov-file#api-documentation)
    - [Retrieving authors](https://github.com/fczanetti/work-at-olist?tab=readme-ov-file#1---retrieving-authors)
    - [Retrieving books](https://github.com/fczanetti/work-at-olist?tab=readme-ov-file#2---retrieving-books)
    - [Retrieving/reading a specific book](https://github.com/fczanetti/work-at-olist?tab=readme-ov-file#3---retrievingreading-a-specific-book)
    - [Creating a new book](https://github.com/fczanetti/work-at-olist?tab=readme-ov-file#4---creating-a-new-book)
    - [Updating a book](https://github.com/fczanetti/work-at-olist?tab=readme-ov-file#5---updating-a-book)
    - [Deleting a book](https://github.com/fczanetti/work-at-olist?tab=readme-ov-file#6---deleting-a-book)
- [Working environment](https://github.com/fczanetti/work-at-olist?tab=readme-ov-file#working-environment)



## Database

```mermaid
classDiagram

    Author "*" <--> "*" Book

    class Author {
        - name: ~string~
    }

    class Book {
        - name: ~string~
        - edition: ~int~
        - publication year: ~int~
        - authors: list~int~
    }
```


## Folder structure

```
├── 📂 work-at-olist
|   ├── 📂 contrib
|   |   ├── env-sample
|   ├── manage.py
|   ├── Pipfile
|   ├── Pipfile.lock
|   ├── authors.csv
|   ├── 📂 work_at_olist
|   |   ├── api.py
|   |   ├── urls.py
|   |   ├── settings.py
|   |   ├── 📂 base
|   |   |   ├── api.py
|   |   |   ├── books.py
|   |   |   ├── models.py
|   |   |   ├── schemas.py
|   |   |   ├── 📂 management
|   |   |   |   ├── 📂 commands
|   |   |   |   |   ├── import_authors.py
|   |   |   ├── 📂 tests
```


## Installing

Follow the next steps to install and run this project.

1 - Clone this repository:
```
git clone git@github.com:fczanetti/work-at-olist.git
```

2 - Create a virtual environment and install the libraries listed in Pipfile. If you are using pipenv, just run the following command:
```
pipenv sync -d
```

3 - If your virtual environment is not yet activated, activate it:
```
pipenv shell
```

4 - Copy the env-sample file to a new file named .env. You can simply create a new file and copy the content from env-sample or, if you are on Linux, use the following command. Remember that you must be on the root diretory before running;
```
cp contrib/env-sample .env
```

5 - Completely remove the DATABASE_URL from the new .env file (variable name and value);

6 - Apply the migrations to the database:
```
python manage.py migrate
```

7 - Start the server:
```
python manage.py runserver
```

By now you should have the project running. You can visit http://127.0.0.1:8000/api/docs to test some requests.


## Installing with Docker

1 - Follow the steps 1 to 4 from the [Installing section](https://github.com/fczanetti/work-at-olist?tab=readme-ov-file#installing); 

2 - On your .env file, adjust the database environment variables to look like this:

```
DATABASE_URL=postgres://user01:pass01@localhost:5438/olistdb
POSTGRES_PASSWORD=pass01
POSTGRES_USER=user01
POSTGRES_DB=olistdb
```

3 - Start the containers.

```
docker compose up -d
```

Now you can visit http://127.0.0.1:8000/api/docs to test some requests.


## Importing authors from .csv

```
python manage.py import_authors authors.csv
```

If you installed using Docker, use this command:

```
docker exec <CONTAINER_ID> python manage.py import_authors authors.csv
```

## Running tests

You can run the tests to make sure everything is working.

```
pytest
```

Use the following command if you installed this project with Docker:

```
docker exec <CONTAINER_ID> pytest
```


## API documentation

Once you have your application running, you can visit http://127.0.0.1:8000/api/docs and test some requests. You can also check in this section some examples.

### 1 - Retrieving authors

To retrieve the authors registered, send a GET request to:
```
http://127.0.0.1:8000/api/authors
```
You can also use some filters to be more specific, for example: 
```
http://127.0.0.1:8000/api/authors?name=Bob&page=1&num_items=10
```
Where:
- name: name of the author;
- page: number of page in case of big responses;
- num_items: number of items to be shown in each page.

If successfull, the response will return in the following format with status code 200.

```
{
  "items": [
    {
      "id": 24,
      "name": "Bob"
    }
  ],
  "num_pages": 1,
  "curr_page": 1
}
```

### 2 - Retrieving books

To retrieve books, send a GET request to:

```
http://127.0.0.1:8000/api/books
```

You can also apply some filters, for example:

```
http://127.0.0.1:8000/api/books?name=Book&edition=1
```

The possible filters are:
- name: name of the book (ex. name=Book);
- edition: edition of the book (ex. edition=1);
- publication_year: publication year of the book (ex. publication_year=2024);
- authors: ID of the author. There can be more than one (ex. authors=2&authors=3);

Choosing page and num_items is also possible here.

If successfull, the response will return in the following format with status code 200.

```
{
  "items": [
    {
      "id": 11,
      "name": "Book",
      "edition": 1,
      "publication_year": 2024,
      "authors": [
        2
      ]
    }
  ],
  "num_pages": 1,
  "curr_page": 1
}
```

### 3 - Retrieving/reading a specific book

To retrieve a specific book, send a GET request informing the ID of the book:

```
http://127.0.0.1:8000/api/books/{book_id}
```

For example: 

```
http://127.0.0.1:8000/api/books/1
```

If successfull, the response will be in this format with status code 200.

```
{
  "id": 1,
  "name": "Book 01",
  "edition": 2,
  "publication_year": 2024,
  "authors": [
    1,
    3
  ]
}
```

### 4 - Creating a new book

To create a book, send a POST request to:

```
http://127.0.0.1:8000/api/books/create
```

The body of the request should be in the following format:

```
{
  "name": "New Test Book",
  "edition": 1,
  "publication_year": 2024,
  "authors": [
    1
  ]
}
```

If successfull, the response will have a 201 status code and the created book will be returned. Also, there will be a response header named 'location' to inform the location of the new book.

```
{
  "id": 13,
  "name": "New Test Book",
  "edition": 1,
  "publication_year": 2024,
  "authors": [
    1
  ]
}
```

### 5 - Updating a book

To update a book, send a PUT request to the following address:

```
http://127.0.0.1:8000/api/books/update/{book_id}
```

The body of the request has to be in this format. Let's suppose we used 13 as the book_id:

```
{
  "name": "New Test Book Updated",
  "edition": 1,
  "publication_year": 2024,
  "authors": [
    1
  ]
}
```

If successfull, the response will have a 200 status code and the following format:

```
{
  "id": 13,
  "name": "New Test Book Updated",
  "edition": 1,
  "publication_year": 2024,
  "authors": [
    1
  ]
}
```

### 6 - Deleting a book

To delete a book, send a DELETE request informing the ID of the book.

```
http://127.0.0.1:8000/api/books/delete/{book_id}
```

Let's suppose we used 13 again as the ID of the book. If successfull, the deleted book will be in the body of the response and the status code will be 200.

```
{
  "id": 13,
  "name": "New Test Book Updated",
  "edition": 1,
  "publication_year": 2024,
  "authors": [
    1
  ]
}
```


## Working environment

In construction