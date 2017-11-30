##Assumptions##

Since this project does not need to do raw queries, Django's ORM protects SQL injection attacks.

This project uses CSRF protection when submitting a new contact.

As we are using Django Forms, it already verifies our "limitations". The name input has a maxlength of 100 and the Email input is of type email, which validates it. Nonethless we also do a verification when data arrives to the server to improve our secutiry.

##Setup and Start Project##

This project uses venv. To install it run:

    python3 -m venv venv

To start venv run: (to exit venv just type 'deactivate')

    source venv/bin/activate

Go to the project folder:

    cd seedstarts

For first time usage and database creation run the following:

    python manage.py migrate

To start the project run:

    python manage.py runserver
