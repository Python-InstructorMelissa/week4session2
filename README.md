# week4session2

# Session:
Add to our server file = app.secret_key = 'some secret key stuff here'
This is needed to help session


You can also pipenv install python-dotenv and put your key into a .env file (thus hidden from github with a .gitignore) and then import os on the server file and change after the = to be something like this --> os.environ['KEY']

Or you can make a env.py file (add this to the .gitignore) add from env import KEY to  your server file and then just put KEY after the =