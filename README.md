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
|   |   |   ├── customizations.py
|   |   |   ├── models.py
|   |   |   ├── schemas.py
|   |   |   ├── 📂 management
|   |   |   |   ├── 📂 commands
|   |   |   |   |   ├── import_authors.py
|   |   |   ├── 📂 tests
```