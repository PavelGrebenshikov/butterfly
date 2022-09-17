# Butterfly

Butterfly is an online cosmetics store

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Run

### Docker

First, you need to make sure you have installed [docker](https://www.docker.com/get-started/) and [docker-compose](https://docs.docker.com/compose/gettingstarted/)

Create _config.env_ file in repository root

Build this locally:

```bash
docker-compose -f base-compose.yaml -f local-compose.yaml build
```

or on production:

```bash
docker-compose -f base-compose.yaml -f production-compose.yaml build
```

**Note:** every docker-compose command should run with -f (--file) flags

Run application:

```bash
docker-compose -f base-compose.yaml -f local-compose.yaml up
```

or Run application in background:

```bash
docker-compose -f base-compose.yaml -f local-compose.yaml up -d
```

Congratulations! You can visit http://127.0.0.1:8000/

After first running you should run all migrations:

```bash
docker-compose -f base-compose.yaml -f local-compose.yaml -w /app python manage.py migrate
```

If you want to terminate containers:

```bash
docker-compose -f base-compose.yaml -f local-compose.yaml down
```

**Note:** Do not worry about your db data after terminating: all data stores in postgres-data folder

### Python

Create virtual enviroment:

```bash
python -m venv venv
source venv/bin/activate
```

Install local requirements:

```bash
pip install -r requirements/local.txt
```

or production:

```bash
pip install -r requirements/production.txt
```

Install os dependencies:

```bash
bash utility/install_os_dependencies.sh
```

Then, create a postgres database on your local machine. Set the enviroment variable DATABASE_URL like this:

```bash
export DATABASE_URL=postgresql://user:password@host:port/dbname
```

Run application locally:

```bash
python manage.py runserver
```

or on production:

```bash
python manage.py runserver --settings config.settings.production
```

Congratulations! You can visit http://127.0.0.1:8000/

After first running you should run all migrations:

```bash
python manage.py migrate
```

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy butterfly

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

## Deployment

The following details how to deploy this application.
