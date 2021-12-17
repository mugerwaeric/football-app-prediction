# tournament-manager
An application for hosting soccer tournaments!

This is a simple Django project to run and manage football (soccer) ⚽ tournaments! It provides the admin the ability to create tournaments, add teams and create fixtures. It also provides a live dashboard with real-time scores and league table! 

## Developer
This project is developed by `Mugerwa Eric` with <a task>ID<Strong> `19` for submission of course-work for course open-source to Mr. Mugerwa.

## Run the application

Navigate to the home directory of this project

`pipenv install` or `pip install -r requirements.txt` to build the required dependencies. (am using python 3.8)

`cd tournament_manager`

`python3 manage.py migrate`

`python3 manage.py runserver`

The expected output will be:
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
December 09, 2021 - 04:12:12
Django version 2.2.4, using settings 'tournament_manager.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
  
## Open Browser
Open your browser in case u want to navigate to the admin section ==> `http://127.0.0.1:8000/admin/login` 
In case you want to navigate to the other part ==> `http://127.0.0.1:8000/admin/`
You will see a login screen
Password ==> 
```
username: erick
password: erick
```



