_# managing_posts

## AMCEF - test assignment

### Installation

1. Download and install python 3.10.6 from https://www.python.org/downloads/

2. Download project from github https://github.com/KikoSokol/managing_posts

3. Switch to directory with project

```sh
cd managing_posts
```

4. Create and activate virtual environment

```sh
virtualenv --python C:\Path\To\Python\python.exe env
.\venv\Scripts\activate
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
