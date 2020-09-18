# django
Django: Python-based open-source web framework that follows the model-template-views architectural pattern.

## INSTALLING Django via pip
```$ python3 -m pip install Django```

### Checking Django version
```
    >>> import django
    >>> django.VERSION
```

### Start a project.
```$ django-admin startproject mysite .```
// don't forget the '.' at the end. run this command inside the project directory

### Overview of the locallibrary project sub-folder
* "manage.py" is a script that helps with management of the site. 
    - (amongst other things) it enables us to start a web server without installing anything else.
* **__init__.py** is an empty file that instructs Python to treat this directory as a Python package.
* **settings.py** contains all the website settings, including registering any applications we create, the location of our static files, database configuration details, etc.  
* **urls.py** defines the site URL-to-view mappings. While this could contain all the URL mapping code, it is more common to delegate some of the mappings to particular applications, as you'll see later.
* **wsgi.py** is used to help your Django application communicate with the webserver. You can treat this as boilerplate.
* **asgi.py** is a standard for Python asynchronous web apps and servers to communicate with each other. ASGI is the asynchronous successor to WSGI and provides a standard for both asynchronous and synchronous Python apps (whereas WSGI provided a standard for synchronous apps only). It is backward-compatible with WSGI and supports multiple servers and application frameworks.
* **NOTE:** *Let's ignore the other files for now as we won't change them. The only thing to remember is not to delete them by accident!*

#### Overview inside an app
* **A migrations folder**, used to store "migrations" — files that allow you to automatically update your database as you modify your models.

### Creating database (sqlite3)
```$ python3 manage.py migrate```
// This goes to the project directory with manage.py

### Run server
```$ python3 manage.py runserver```

HOORAY!!! The first Django web app is up and running.
<a href="url"><img src="https://github.com/RocqJones/django/blob/master/imgs/django.png" height="400" width="100%" ></a>

# Deep Dive.
## How Django code looks like in details.
Django web applications typically group the code that handles each of these steps into separate files:
<a href="url"><img src="https://github.com/RocqJones/django/blob/master/imgs/basic-django.png" height="400" width="50%" ></a>

* **URLs:** While it is possible to process requests from every single URL via a single function, it is much more maintainable to write a separate view function to handle each resource. *A URL mapper is used to redirect HTTP requests to the appropriate view based on the request URL.* The URL mapper can also match particular patterns of strings or digits that appear in a URL and pass these to a view function as data.
* **View:** A view is a request handler function, which receives HTTP requests and returns HTTP responses. Views access the data needed to satisfy requests via models, and delegate the formatting of the response to templates.
* **Models:** Models are Python objects that define the structure of an application's data, and provide mechanisms to manage (add, modify, delete) and query records in the database. 
* **Templates:** A template is a text file defining the structure or layout of a file (such as an HTML page), with placeholders used to represent actual content. A view can dynamically create an HTML page using an HTML template, populating it with data from a model. A template can be used to define the structure of any type of file; it doesn't have to be HTML!.

### 1. Sending the request to the right view (urls.py)
The mapper  (```urlpatterns```) defines a list of mappings between routes (specific URL patterns) and corresponding view functions. *If an HTTP Request is received that has a URL matching a specified pattern then the associated view function will be called and passed the request.*

### 2. Handling the request (views.py)
Like all view functions it receives an ```HttpRequest``` object as a parameter (```request```) and returns an ```HttpResponse``` object.

### 3. Defining data models (models.py)
Models define the structure of stored data, including the field types and possibly also their maximum size, default values, selection list options, help text for documentation, label text for forms, etc. 
* The definition of the model is independent of the underlying database — you can choose one of several as part of your project settings. 
* Once you've chosen what database you want to use, you don't need to talk to it directly at all, you just write your model structure and other code, and Django handles all the dirty work of communicating with the database for you.

### 4. Querying data (views.py)
The Django model provides a simple query API for searching the database. This can match against a number of fields at a time using different criteria (e.g. exact, case-insensitive, greater than, etc.), and can support complex statements (for example, you can specify a search on U11 teams that have a team name that starts with "Fr" or ends with "al")

### 5. Rendering data (HTML templates)
Template systems allow you to specify the structure of an output document, using placeholders for data that will be filled in when a page is generated. 
* Templates are often used to create HTML, but can also create other types of document. 
* Django supports both its native templating system and another popular Python library called Jinja2 out of the box (it can also be made to support other systems if needed). 

## Just a few of the other things provided by Django include:
* **Forms:** HTML Forms are used to collect user data for processing on the server. Django simplifies form creation, validation, and processing.
* **User authentication and permissions:** Django includes a robust user authentication and permission system that has been built with security in mind.
* **Caching:** Creating content dynamically is much more computationally intensive (and slow) than serving static content. Django provides flexible caching so that you can store all or part of a rendered page so that it doesn't get re-rendered except when necessary.
* **Administration site:** The Django administration site is included by default when you create an app using the basic skeleton. It makes it trivially easy to provide an admin page for site administrators to create, edit, and view any data models in your site.
* **Serialising data:** Django makes it easy to serialise and serve your data as XML or JSON. This can be useful when creating a web service (a website that purely serves data to be consumed by other applications or sites, and doesn't display anything itself), or when creating a website in which the client-side code handles all the rendering of data.