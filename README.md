# test-me
Python Africa - Django Testing Workshop

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

## Selenium tests
If you want to run full integration test you can use Selenium.
This will use a special version of Chrome to test your website.

### First install ChromeDriver
OSX: `brew cask install chromedriver` if you have brew installed (which you should)
Windows / Linux / OSX:
Get the latest ChromeDriver here: http://chromedriver.storage.googleapis.com/index.html 
Extract the zip file that fits your OS and put it somewhere where your commandline can reach it and make sure it is executable.

### Start testing
Open settings file `testme/settings/base.py` and change `SELENIUM_TESTS_ENABLED = False` to `SELENIUM_TESTS_ENABLED = True`.
Now your tests will also run a full stack test!





