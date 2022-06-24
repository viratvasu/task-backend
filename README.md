## Django Backend

### How to install and run locally
1. Clone the repo
2. create virtual environment
3. install all the dependepncies by `pip install -r requirements.txt` which you can find in root directory
4. Change Default DB URLS in settings.py file (Using Postgres). you can use default sqlite3 if you don't have postgreSQL installed
To use Sqlite3 replace with this code in `settings.py/DATABASES`
```python
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
```
5. After configuring all the DB settings. You can do migrations with command `python manage.py migrate` in root directory where manage.py exist
6. You can create a user by command `python manage.py createsuperuser` enter username, email, password. User created to authenticate on client(react)
7. Run the dev server with command `python manage.py runserver` which will run by default on `http://127.0.0.1:8000`
8. I have impleted some unit testing as well you can use `python manage.py test` to check them
9. Before parsing data on frontend you should have `UserProfile` obejcts at at least 10 (max userId in json file provided)
10. To create simply go to django shell with the help of  `python manage.py shell`. Then write this small script which will create 100 UserProfile objects with name `TestUser`
```python
from application.models import UserProfile
for i in range(100):
    UserProfile.objects.create()
```

