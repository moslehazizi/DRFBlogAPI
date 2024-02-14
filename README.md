This is a back-end RESTful api service for a blog with Django-Rest-Framework. All CRUD operations are considered. It comes with powerful token based authentication.
'SwaggerUI' tool added for document apis.

Setup
First clone the project:

  $ git clone https://github.com/moslehazizi/DRFBlogAPI.git
  $ cd DRFBlogAPI

Then create a virtual environment to install dependencies in and activate it:

  $ virtualenv env
  $ source env/bin/activate

Now You must see the (env) in front of the prompt. Then install dependencies:

  (env)$ python -m pip install -r requirements.txt

Migrate model to database:

  (env)$ python manage.py migrate

And runserver by:

  (env)$ python manage.py runserver

You can create superuser and see django admin panel. Head over web browser and see schema of all apis in the blog:
http://127.0.0.1:8000/api/schema/swagger-ui/

