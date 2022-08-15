_# managing_posts

## AMCEF - test assignment

### Installation - Database PostgreSQL

1. Download installer from https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

2. Install PostgreSQL
- In installation wizard you must choose PostgreSQL and pgAdmin 4
- You must set password "postgres" and user "postgres" in installation wizard
- You must set port to 5432
- In pgAdmin 4 application you must create database with name "managing_posts"
- You may set previous parameters to other value, but you must change database settings in file /managing_posts/settings.py



### Installation - Application

1. Download and install python 3.10.6 from https://www.python.org/downloads/

2. Download project from github https://github.com/KikoSokol/managing_posts

3. Switch to directory with project

```sh
cd managing_posts
```

4. Create and activate virtual environment

```sh
virtualenv --python C:\Path\To\Python\python.exe env
.\env\Scripts\activate
```

5. Install all dependencies:
```sh
(env)$ pip install -r requirements.txt
```

6. Run application:

```sh
(env)$ python manage.py runserver
```

The application should run at http://127.0.0.1:8000/

#### Documentation API:

Swagger: http://127.0.0.1:8000/swagger/

ReDoc: http://127.0.0.1:8000/redoc/
