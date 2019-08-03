# test-me
Python Africa - Django Testing Workshop

Make sure you get Chromedriver and put it in your PATH

http://chromedriver.storage.googleapis.com/index.html

After you cloned this repository:

```
pip install -r requirements.txt
```

You could also use virtualenv or virtualenvwrapper to have your installation in a separate directory.


## Running the project

First make sure to migrate the database:
```
python manage.py migrate
```
Create a superuser
```
python manage.py createsuperuser
```
Now run the server

```
python manage.py runserver
```

## Now for some testing

Run tests using

```
python manage.py test
```
You can also run specific tests
```
python manage.py test apps.users.tests.UserTests.test_full_name
```

