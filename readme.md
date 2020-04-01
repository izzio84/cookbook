# Create Django APP
## Install Django
***
## Make virtual env

#### create a dir
#### install virtual env  
    pip install virtualenv
#### inside dir create your env
    virtualenv myenv
#### activate your env
In Win
     
     myenv\Scripts\activate.bat
In mac/linux
    
    source myenv/bin/activate

#### to deactivate:

    deactivate
***
## Installing Django In The Virtual Environment
    pip install Django
***
## Setting Up The Project
    cd Desktop
    mkdir mysite
    cd mysite
    django-admin startproject mysite
    cd mysite
    python manage.py startapp blog  
    python manage.py runserver

Now add the newly created app blog at the bottom and save it.
    
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'blog'
    ]

and then 

    (django) $ python manage.py makemigrations 
    (django) $ python manage.py migrate
***
## Creating An Administration Site

    python manage.py createsuperuser
***
## Using PostgreSQL with Django

#### Installing PostgreSQL
Windows and macOS X users can download PostgreSQL from the official site https://www.postgresql.org/download/ and simply install it.

Note that tutorial is strictly based on Python 3

#### Linux User
    sudo apt-get install postgresql postgresql-contrib
Also, Linux users need to install some dependencies for PostgreSQL to work with Python.

    sudo apt-get install libpq-dev python3-dev
#### Install psycopg2
Next, we need to install the PostgreSQL database adapter to communicate to the database with Python to install it run the following command in the shell.

    pip install psycopg2
#### Create A PostgreSQL User and Database

#### Creating Database
    CREATE DATABASE mydb;
This will create a database named mydb, note that every SQL statement must end with a semicolon.

#### Creating User
    CREATE USER myuser WITH ENCRYPTED PASSWORD 'mypass';
Here we are creating a user named myuser with password mypass. You can use any username and password you wish.

#### Modifying Connection Parameters
    ALTER ROLE myuser SET client_encoding TO 'utf8';
    ALTER ROLE myuser SET default_transaction_isolation TO 'read committed';
    ALTER ROLE myuser SET timezone TO 'UTC';
#### Granting Permission To The User
    GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;

## Integrating PostgreSQL With Django
Open the settings.py file of your project and scroll straight to the database section, which should look like this.

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
We need to update these settings to integrate our PostgreSQL with the project.

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'mydb',
            'USER': 'myuser',
            'PASSWORD': 'mypass',
            'HOST': 'localhost',
            'PORT': '',
        }
    }
***
## Managing Media Files in Django

#### Configuring Media Files in Django
Open settings.py file of your project and add the following configuration.

    # Base url to serve media files
    MEDIA_URL = '/media/'

    # Path where media is stored
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL is the URL that will serve the media files.

During development, it doesn’t matter much as long it doesn’t conflict with any view of the apps. In production, uploaded files should be served from a different domain such as Amazon S3.

MEDIA_ROOT is the path to the root directory where the files are getting stored.

#### Serving Media Files in Development
By default, Django doesn’t serve media files during development( when debug=True).

In order to make the development server serve the media files open the url.py of the project and make the below changes.

    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns = [
        path('admin/', admin.site.urls),
        ...
    
    ]
    if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)
That’s all now, run the local development server add files in the media root folder and retrieve them from media URL.
***
