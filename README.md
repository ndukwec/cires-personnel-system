**CIRES Personnel Management System**

Stack: Django (Python), JavaScript, HTML, CSS (Bootstrap)
Database: Postgres

This is a simple pms, built with django. we have a model called Personnel with first name, last name, employee number
and academic qualification attributes. 

**To run this project, do the following:**

a.) Make sure you have Python installed

b.) Make sure you have Postgres installed
    b.1) Make sure you have created a user in your database with name 'cires' and password 'notsosecurepassword1!'
    b.2) Make sure you have created a database called cires
    b.3) Be sure to grant all privileges to user cires on database cires

c.) Run you migration -- python manage.py migrate

d.) Run the server on port 8000 -- python manage.py runserver 0.0.0.0:8000

I should be able to automate all of the above in a shell script and I will at some point but for now just follow the
instructions above.

_I will also be using Django CMS, more on that to come_
