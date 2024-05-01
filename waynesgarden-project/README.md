# Django Forms - Django Pizza Project

## Table of Contents
1. [Starting the Project](#starting-the-project)
2. [Making Forms from Scratch](#making-forms-from-scratch)

## Starting the Project

### Step 1. Install virtualenv
```console
pip3 install virtualenv
```
### Step 2. Create Virtual Environmet
Make sure you are in the directory where you want to install the virtual environment before running the below code.
```console
virtualenv venv
```

### Step 3. Start the Virtual Environment
**For Windows**
```console
source venv/Scripts/activate
```

**For Mac**
```console
source venv/bin/activate
```
### Step 4. Install Django
```console
pip install django
```
### Step 5. Start Django Project
```console
django-admin startproject waynesgarden-project
```
**Move into the project folder**
```console
cd waynesgarden-prject
```
**Run the project**
```console
python manage.py runserver
```
Now when you visit: http://127.0.0.1:8000/ you should see that your page looks like the image below
![Django Start Page](django-start-page.jpg)

## Making Forms from Scratch
### Step 1. Create a New App
Be sure to move out of your project directory, back into the parent before running this code.
```console
django-admin startapp pizza
```
### Step 2. Modify the urls.py file
Open up your code editor (I'm using VSCode) and navigate to the
waynespizza-project > waynespizza directory and open urls.py

- Import module
```python
from pizza import views
```
- Create paths in the ``urlpatterns[] list``
```python
urlpatterns = [
    path("admin/", admin.site.urls),
    # add home and order paths. leaving home path as an empty string
    path('', views.home, name='home'),
    path('order', views.order, name='order'),
]
```
### Step 3. Modify Settings file
Now open up the settings.py file and add the ```pizza``` app to the ```INSTALLED_APPS[] list```
```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "pizza", # add pizza app here
]
```
### Step 4. Create views
- Move into the pizza app folder and open views.py and create views for the home and order page
```python
# Create view for home page
def home(request):
    return render(request, 'pizza/home.html')

# Create view for order page
def order(request):
    return render(request, 'pizza/order.html')
```
### Step 5. Create templates for the home and order pages
Create a ``templates`` folder inside the pizza app directory and then a ``pizza`` folder inside the ``templates`` directory (templates >> pizza) and 2 files inside the ``pizza`` direcory (home.html and orders.html) See the structure below.

- templates
    - pizza
        - home.html
        - orders.html
- Content for home.html
```html
<h1>Wayne's Garden</h1>
    <a href="{% url 'order' %}">Order a pizza</a>
```
- Content for order.html
```html
<h1>Order a pizza</h1>
```