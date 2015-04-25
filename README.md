# start-my-django
A script that starts your django project in correct way i.e starts your virtualenv, starts django project, starts app and also initializes git.
Forget the pain of doing all of these steps one-by-one manually.The script does everything for you


Requirements:

    1) Python (2.7 or greater)
    2) VirtualEnv (pip install virtualenv)
  
How to run the script:
   
    1) Create the folder in which you would like to store your django project (mkdir /path/to/folder) 
    and navigate to that folder
    2) Copy the 'start-my-django.py' file into that folder
    3) Then run python start-my-django.py

What script does:

    1) When you run the script, it will first install and activate virtual env in the current folder
    2) It will then prompt you to install django. If you wish to proceed, then it installs Django
    3) Once django installation is done, it asks for the django project name and starts the project
    4) After the project is started, it asks for app name and starts the app
    5) Once the app is started, it will ask if you wish to do git initialization. If yes, 
    then it initializes git in the current folder and makes the first commit.
    6) You can use the script to start any number of django projects.
    
I have tested script against bare minimum combinations of bad-inputs. Please report the issues incase the script fails 
due to bad inputs
    
