# DRFD Level One -- What you will learn
1. how to use the Django REST Framework to create REST APIs
2. Understand the concepts of Serialization and Deserialization
3. How to use the Serializer and ModelSerializer classes
4. How to create Function/Class Based API Views
5. What the Browsable API is and how to use it
6. Define validation criteria for user input
7. How to properly represent nested relationships between entities with DRF

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# What is Django REST Framework?
Django REST Framework is a powerful and flexible toolkit for building Web APIs with Python and Django.

IMPORTANT We can install it via pip and include it in any existing Django Project just by adding “rest_framework” to the INSTALLED_APPS list.

NB Django REST Framework is not a modified version of Django!

Django REST Framework allows us to create powerful production ready Web APIs in a very short time, with all the support and advantages of the Python and Django ecosystems and communities. It’s the number one package for creating REST APIs with Django, used by world class companies such as Mozilla, Heroku, Red Hat and Eventbrite.

Django REST Framework intentionally uses many of Django’s programming conventions, making it a natural extension of the package that is easy to pick up and understand.In this lesson we are going to create a new Django Project that we are then going to use throughout the section, learning how to use all of DRF’s main components by creating a Web API for a news website.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# NB 1) --> WHAT-TO-DO Setup and installation

- create new env with venv, then activate it

- install django and DRF
>>> pip install django
>>> pip install djangorestframework

- create new django project
>>> django-admin startproject newsapi

- navigate into the newsapi folder
>>> cd newsapi

- create new app
>>> python manage.py startapp news

- go to newsapi/setting.py and add: "rest_framework", "news"

- create models then create the migrations
>>> python manage.py makemigrations
>>> python manage.py migrate

- create superuser
>>> python manage.py createsuperuser

- register the models in admin.py

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Serializers
IMPORTANT Serializers allow complex data such as querysets and model instances to be converted to native Python data types that can then be easily rendered into useful formats like JSON: this process is known as Serialization of Data.

Serializers are a very important component of DRF, that we can easily use by employing the Serializer and ModelSerializer classes.

Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.

In this lesson we are going to learn how to use the  Serializer class to serialize/deserialize data from our Article model.

We are also going to briefly talk about Parsers and Renderers. 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# NB 2) --> WHAT-TO-DO

- create a new folder named "api" inside of the "news" application --> in this folder we will add all the files that will be part of the API itself --> this is the BEST PRACTICE --> in this folder, create the serializers.py file
