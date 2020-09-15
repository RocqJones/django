# django
Django: Python-based open-source web framework that follows the model-template-views architectural pattern.

## INSTALLING Django
    ```$ python3 -m pip install Django```

## CHECKING Django version
```
    >>> import django
    >>> django.VERSION
```

## START A PROJECT
    ```$ django-admin startproject mysite .```
    // don't forget the '.' at the end. run this command inside the project directory

## OVERVIEW
* "manage.py" is a script that helps with management of the site. 
    - (amongst other things) it enables us to start a web server without installing anything else.
* "settings.py" file contains the configuration of your website.
* "urls.py" file contains a list of patterns used by urlresolver.
* **NOTE:** *Let's ignore the other files for now as we won't change them. The only thing to remember is not to delete them by accident!*

## CREATING DATABASE (sqlite3)
    ```$ python3 manage.py migrate```
    // This goes to the project directory with manage.py

## RUN SERVER
    ```$ python3 manage.py runserver```

HOORAY!!! The first Django web app is up and running.
<a href="url"><img src="https://github.com/RocqJones/django/blob/master/imgs/django.png" height="400" width="100%" ></a>
