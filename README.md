# Bookmarkr
---------
An app to create lists of web bookmarks

## Getting set up
1. In your terminal, navigate to the directory you would like the app to live in
2. Still in your terminal, execute the code `git clone https://github.com/jluria/bookmarkr.git` to clone this repository
3. `cd` into that directory and create your virtual environment using [virtualenv](https://pypi.python.org/pypi/virtualenv)
  * If you don't have virtualenv, you can install it via pip
  * Many people call their virtual environment directory `env`
4. Activate your virtual environment by running `source env/bin/activate`
5. Run the command `pip install django` to install Django
6. Run the command `python manage.py migrate` to migrate the existing migrations and create the database
7. Run the command `python manage.py runserver` to run the local webserver
8. Run the command `python manage.py createsuperuser` and follow the prompts to create an admin login
9. Open a browser and navigate the localhost:8000/admin to log in to the admin site and create a public account user
10. Navigate to localhost:8000/ and log in to begin using the app!

## Assumptions made in the design choices
