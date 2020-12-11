# softuni_final_project
Final SoftUni Django project

##Setup
The first thing to do is to clone the repository:

$ git clonehttps://github.com/PetarGeorgi/softuni_final_project.git
$ cd softuni_final_project.git

Create a virtual environment to install dependencies in and activate it:

$ virtualenv2 --no-site-packages env
$ source env/bin/activate

Then install the dependencies:

(env)$ pip install -r requirements.txt
Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv2.

Once pip has finished downloading the dependencies:

(env)$ cd myclub_project/myclub_site
(env)$ python manage.py runserver

## Navigation
And navigate to http://127.0.0.1:8000/ or htttp://127.0.0.1:8000/contact to see the public part of the django template.
Private part (accessible only by authenticated user and admins) after register http://127.0.0.1:8000/register/ and log in on http://127.0.0.1:8000/login/
