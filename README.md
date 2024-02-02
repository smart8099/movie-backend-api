# Movie Backend App

This is the backend (CRUD) app for a simple VueJS application built with the purpose of understanding routing and state management in vue. This app provide a simple REST API endpoints to be used in the frontend. Movie Data is being served via REST API from a backend application in django using djangorestframework. Fixtures containing sample data was uploaded in the db.

## Built With

-Python
-Django (djangorestframework)

## Getting Started

To get a local copy up and running follow these simple example steps.

- python3
- Git

### Setup

    git clone https://github.com/smart8099/movie-backend-api.git

### Create virtual environment

    python3 -m venv myvenv

### Activate virtual environment

    source  myvenv/bin/activate

### Install Dependencies

    pip install -r requirements.txt

### Load fixture

    python3 manage.py loaddata data.json

### Run application

    python3 manage.py runserver

### REST APIs endpoints

    http://localhost:8000/api/movies/ [GET,POST]
    http://localhost:8000/api/movies/<int:id> [GET,PUT,PATCH,DELETE]
    http://localhost:8000/api/movies/?search= [Filtering]

### Allowed CORS origin
    "http://localhost:5173",
    "http://localhost:5174",
    "http://127.0.0.1:9000",

## Authors

👤 Abdul Basit Mohammed

GitHub: @smart8099

- GitHub: [smart8099](https://github.com/smart8099/)
- LinkedIn: [Abdul Basit Mohammed](https://www.linkedin.com/in/abdul-basit-mohammed-40b973185/)
