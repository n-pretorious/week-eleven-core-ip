# Neighborhood watch
A web app that helps you stay in touch with your neighborhood.


## Core Features

* Admin can add/remove a neighborhood.
* A user can sign in with the application to start using.
* A user can set up a profile and a general location and my neighborhood name.
* A user can find a list of different businesses in their neighborhood.
* A user can find Contact Information for the health department and Police authorities near their neighborhood.
* A user can create Posts that will be visible to everyone in my neighborhood.
* A user can only view details of a single neighborhood.
* A user can change My neighborhood when I decide to move out.

## Prerequisites

* Python3
* Django
* Postgres

## Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/<username>/<project_name>.git
    $ cd <project_name>

## Usage

### Activate the virtual enviroment for your project

    $ python3 -m venv --without-pip virtual
    $ source virtual/bin/activate

Download the latest version of pip in virtual our environment

    $ curl https://bootstrap.pypa.io/get-pip.py | python

Install project dependencies:

    $ pip install -r requirements.txt

### Setup database

    $ psql
    $ CREATE TABLE <table_name>;

### Setup cloudinary

If you don't have an account proceed to [https://cloudinary.com/users/register/free] and register to get cloudinary account details

## Environment variables

The `ENVIRONMENT` variable loads the correct settings. Fill in the correct credentials

    ```.env
    CLOUD_NAME=''
    API_KEY=''
    API_SECRET=''
    SECRET_KEY=''
    DEBUG=bolean
    DB_NAME='instclone'
    DB_USER=''
    DB_PASSWORD=''
    DB_HOST=''
    MODE=''
    ALLOWED_HOSTS='*'
    DISABLE_COLLECTSTATIC=''
    ```

Then simply apply the migrations:

    $ python3 manage.py migrate
    $  python3 manage.py makemigrations <app_name>

Run tests:
    $ python3 manage.py test <app_name>

You can now run the development server:

    $ python3 manage.py runserver

## BDD

| BEHAVIOUR    | INPUT   |  OUTPUT |
| :------------- | :------------- | :--------------- |
| User updates profile | New detail | Profile updates |
| User posts a post | Post| Post is displayed |
| User posts his business |  Business post | Posts appear in the business route |


## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Copyright (c) 2020 Pretorious Ndung'u
