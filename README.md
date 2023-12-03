# Batikpedia
Whatzup!!~ This is the Batikpedia backend with Django REST Framework and Firestore.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development purposes. See deployment for notes on how to deploy.
1. Create your own `.env` file in the root directory. Follow the environment format from `.env.example` file.
2. Create your virtual environment (venv), then open terminal at the root directory, activate your venv, and enter `~$ pip install -r requirements.txt`.
3. In terminal, enter `~$ python initialize.py` to initialize pre-configuration files.
4. Run `python manage.py runserver`

The server should be running on localhost:8000.
*Note that the `initialize.py` is not used in settings.py because it does pre-run things, such as generate configuration files, inject dependencies, etc.*

## Deployment
Coming soon.