
# Step 1 --> create django project
Start django project:
>>> django-admin startproject onlinestore

# Steo 2
go into the django project folder and run routine operations:
>>> python manage.py migrate
>>> python manage.py createsuperuser
(NB for website that are going to be deployed in production, use a strong password)

# Step 3
NB cool setting for launching django in debug mode! cfr video


# Step 4 --> create app
inside the django project folder (in 02-Django-api/onlinestore)
>>> python manage.py startapp products
in onlinsestore/settings.py add the "products" app to the list of installed apps

# Step 5
in onlinestore/products/models.py --> add the models that you need for the application
after editing the models, generate the migrations with
>>> python manage.py makemigrations
apply them with
>>> python manage.py migrate

# Step 6
create the templates folder (products/templates) and a subfolder named products

# Step 7
create the views in the views.py file of our app (which is products)

# Step 8
fill in the templates

# Step 9
create the url paths
in the products (app) folder create the urls.py file

# Step 10
include the urls.py file of the products app within the urls.py file of the main project

# Step 11
since we are using media files (images), we also need to tell django that we want our development server to serve media files during the development phase --> cfr the main urls.py file + add some settings in settings.py

# Step 12
configure the admin.py file
which allows us to create new instances of products and manufacturers from the admin interface

