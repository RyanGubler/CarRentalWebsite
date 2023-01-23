# Dans Shady Business
This web app creates a car rental service in which users can rent cars for 
a specified number of days.
## Workspace layout
Dans Shady Business will be stored as a web app in this repository.   

Documentation will be kept in a directory called ""   

Project will be kept in a directory called "dansshadybusiness"   

## Version-control procedures
Each group member should have a forked repository of the app in Ryan's account of the project "cs3450_group-4" in their Github. Each group member should have a cloned version of this repository, and will submit pull requests to monitor progress.

## Tool stack description and setup procedure
Django is our groups framework of choice for this app. We all have experience using Django, and the SQLLite database that is included with Django.

## Build instructions
Clone the project in git bash. `` $ git clone https://github.com/RyanGubler/cs3450_group4 ``   
Migrate in bash `` $ python manage.py migrate ``   
Finally, ``$ python manage.py runserver ``   
Navigate in the browser to [localhost:8000](localhost:8000) to view the app.   
## Unit testing instructions
Unit tests will cover all of the use case diagrams located in Requirements_definition.docx  
Unit tests can be found in the unittests.py file.   
The unit test class will prompt the user to select which test should be performed.   
The following tests will be offered  
1. User renting car  
2. Car pickup
3. User adds money to wallet  
4. Manager hires new employee  
5. Manager purchases new car
6. Manager pays employees
7. Service Call
8. Overdue car is lojacked  
At the end of each test run, results will be displayed to the user.  
## System testing instructions
Start by running `` $ python manage.py runserver`` in the app directory.  
Now that the app is running, navigate to [localhost:8000](localhost:8000).  
Login using the username SystemTest and the password systest.  
These credentials will allow for the user to perform actions as a customer, employee, manager, or owner in a test environment.  

## Other development notes, as needed
