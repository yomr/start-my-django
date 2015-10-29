import os
import subprocess
import re
import sys
yes = re.compile("yes|Y|y|Yes")


      
def install_django(virtualenv_directory):
    try:
        print "Installing django....."
        subprocess.call(['{0}/bin/pip'.format(virtualenv_directory), "install","django"])   
    except Exception,e:
        print "Unable to Install Django.",e
        exit()


def get_project_name():
    print '******************************************** \n'
    django_project_name = raw_input("Please enter the django project name.  Please use only numbers, letters and underscores. \n")
    return django_project_name


def start_project(django_project_name, virtualenv_directory):
    print "Starting django project....."
    try:
        command_run = subprocess.call(["{0}/bin/django-admin.py".format(virtualenv_directory), "startproject", django_project_name])    
    except CommandError as e:
        command_run = 1 #random digit assignment to make the below condition false
    if command_run == 0:  
        print "Project Successfully Started" 
        return True
    else:
        return        


def start_app(django_project_name, virtualenv_directory):
    print '******************************************** \n'
    django_app_name = raw_input("Please enter the App name. The app name should be different from project name. Please use only numbers, letters and underscores. \n")
    os.chdir(django_project_name)
    os.getcwd()
    try: 
        command_run = subprocess.call(["../{0}/bin/python".format(virtualenv_directory), "manage.py", "startapp", django_app_name])
    except Exception as e:
        command_run = 1
    if command_run == 0:   
        print "App Successfully Started"
    else:
        os.chdir('../')
        start_app(django_project_name, virtualenv_directory)        


def start_git():
    print '******************************************** \n'
    print "Before you start writing code, you should know that, \nYour life will be difficult if you do not use Version Control System. Start using Git."
    git_confirm = raw_input("Do you want to go ahead with git initialization(yes/no) \n")
    if yes.match(git_confirm):
        try:
            os.chdir('../')
            subprocess.call(["touch",".gitignore"])
            with open(".gitignore", "w") as f:
                f.write("bin/\nlib/\nlocal/\ninclude/\n*.pyc")
            subprocess.call(["git", "init"])
            subprocess.call(["git", "add", "."])
            subprocess.call(["git", "commit", "-m", "first commit"])
            print "\nGreat work buddy. Git iniitalised and first commit done. You are now safe under the wings of git"
        except Exception,e:
            print "Couldnt initialise Git",e    
            exit()
    print "\nGreat work buddy. You can code now."


def start_virtualenv():
    confirm = raw_input("Welcome to installation. First up, lets install virtualenv.\n Do you want to install in current directory(yes/no) \n")
    confirm = yes.match(confirm)
    if confirm:
        virtualenv_directory = '.' 
    else:
	   virtualenv_directory = raw_input("Please Enter a directory name \n")

    py_version = raw_input("Which Python version do you want to use(2/3) \n")
    py_path = "python" + py_version
    
    try:
        subprocess.call(["virtualenv", "-p", py_path, virtualenv_directory,])
    except OSError, ex:
        print "Something went wrong with the directory path.Please check your directory path",ex
        sys.exit()

    print "\nAwesome. VirtualEnv is installed."        
    return virtualenv_directory


def main():
    virtualenv_directory = start_virtualenv()
    print '******************************************** \n'
    
    confirm = raw_input("Do you want to continue with Django installation(yes/no) \n")
    confirm = yes.match(confirm)
    
    project_success = False
    if confirm:
        install_django(virtualenv_directory)
        while(not project_success):
            project_name = get_project_name()
            project_success = start_project(project_name, virtualenv_directory)
        start_app(project_name, virtualenv_directory)
        start_git()


#start everything
main()