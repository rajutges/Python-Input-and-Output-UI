# Revogreen_Assignment

# Task 

Create 2 different Python UI, one will act as input and another will be as output.

For screen one (input screen): 
This screen will take input in two forms,
a. Entering data through keyboard
b. Slider (From a range of 0-100)

This data should be stored in a database

For the second screen (Output screen):
Fetch the data from the database and display this data on a database.

UI Project
==========
Python Django UI 

INSTALLATION
============
- Clone repository via: 'git clone https://github.com/rajutges/Revogreen_Assignment'

Django Installation & Tutorial
==============================
- https://www.djangoproject.com/download/
- https://docs.djangoproject.com/en/1.4/intro/tutorial01/


Database Setup (MySQL)
======================
  CREATE DATABASE gui DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci; CREATE USER 'gui'@'%' IDENTIFIED BY 'gui'; GRANT ALL PRIVILEGES ON gui . * TO 'gui'@'%';


Server Setup
============
- python manage.py syncdb
- python manage.py runserver

Default Server URL
==================
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/admin/
