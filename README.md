[![codecov](https://codecov.io/gh/fczanetti/work-at-olist/graph/badge.svg?token=FW6xWklGdj)](https://codecov.io/gh/fczanetti/work-at-olist)
![CI](https://github.com/fczanetti/work-at-olist/actions/workflows/work_01.yml/badge.svg)

![Python](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Ffczanetti%2Fwork-at-olist%2Fmain%2FPipfile.lock&query=%24._meta.requires.python_version&label=Python&labelColor=%232b5b84&color=%233d3d3e)
![Django](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Ffczanetti%2Fwork-at-olist%2Fmain%2FPipfile.lock&query=%24%5B'default'%5D%5B'django'%5D%5B'version'%5D&label=Django&labelColor=%230c3c26&color=%233d3d3e)
![Django Ninja](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Ffczanetti%2Fwork-at-olist%2Fmain%2FPipfile.lock&query=%24%5B'default'%5D%5B'django-ninja'%5D%5B'version'%5D&label=Django%20Ninja&labelColor=%234cae4f&color=%233d3d3e)


# Work at Olist

Welcome to work-at-olist project documentation!

This project was developed to solve the challenge proposed by Olist. It consists of an API to store names of authors and books written by them. The requirements were to create a management command to import and save the names of the authors from a .csv file, and also a CRUD to manage the books. An important detail is that a book can be written by more than one author, so a many-to-many relations was used to create the database. Some filters were also created to retrieve books or authors, but these were optional.

More details can be checked in [their requirements](https://github.com/fczanetti/work-at-olist/blob/main/olist_instructions.md). You can also visit the [original repository](https://github.com/olist/work-at-olist).


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

In construction


## Working environment

In construction