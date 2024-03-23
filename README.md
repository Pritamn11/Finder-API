# How to run?

### STEPS: 

Clone the repository 

```bash
https://github.com/Pritamn11/finder-API
```

#### STEPS 01 - Create a virtual environment after opening the repository

```bash
python -m venv newenv
```

```bash
.\newenv\Scripts\activate
```

#### STEPS 02 - Install the requirements

```bash
pip install -r requirements.txt
```

#### STEPS 03 -Set Up PostgreSQL Database

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

```


#### STEPS 04 - Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

#### STEPS 05 - Start the Development Server

```bash
python manage.py runserver
```

### Usage Instructions

 1) Use the specified API endpoint (/api/events/{latitude}/{longitude}/{date}/) to retrieve events for a specific date and location.

 2) Replace {latitude}, {longitude}, and {date} with appropriate values in the API URL.
    
 3) Ensure that the external API for weather conditions and distance calculations is accessible and functioning properly.

 4) Test the API endpoints using tools like Postman, or by making HTTP requests from your application.