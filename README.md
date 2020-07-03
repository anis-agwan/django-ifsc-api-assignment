## Django-ifsc-api-assignment
Created a REST service that can:
1. Given a bank branch IFSC code, get branch details
2. Given a bank name and city, gets details of all branches of the bank in the city

# Steps:
```bash
$ git clone https://github.com/anis-agwan/django-ifsc-api-assignment.git
$ python3 -m venv ifsc-api-django
$ source ifsc-api-django/bin/activate
$ pip install -r requirements.txt
$ cd django-ifscr-api-assignment
$ python manage.py runserver
```

In your browser, visit the URL:
```
http://localhost:8000/import
```
And import the bank_branches.csv to load the Bank and Branch details to the database

Given a bank branch IFSC code, get branch details from the URL:
```
http://localhost:8000/api/ifsc/<ifsc_code>
```

Given a bank name and city, gets details of all branches of the bank in the city from the URL:
```
http://localhost:8000/api/branches/<branchCity>/<bank-name}>
```

API has been deployed on Heroku:
Test it on
```
https://bank-api-ifsc.herokuapp.com/api/ifsc/BARB0MALAPP
```
Issue with the Heroku deployed api is: Not all the csv data has been uploaded 

