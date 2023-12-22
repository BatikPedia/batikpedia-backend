# Batikpedia
Whatzup!!~ This is the Batikpedia backend with Django REST Framework and Firestore.

## Setting Up The Application
Set Up The Following Instances:
1. Firebase Application
2. Google CloudSQL (MySQL)
3. Google Cloud Storage Bucket

Before running the application, here are some GitHub secrets need to be set (can be separated for staging and prod):
1. FIREBASE_SERVICE_ACCOUNT_KEY_TYPE
2. FIREBASE_SERVICE_ACCOUNT_KEY_PROJECT_ID
3. FIREBASE_SERVICE_ACCOUNT_KEY_PRIVATE_KEY_ID
4. FIREBASE_SERVICE_ACCOUNT_KEY_PRIVATE_KEY
5. FIREBASE_SERVICE_ACCOUNT_KEY_CLIENT_EMAIL
6. FIREBASE_SERVICE_ACCOUNT_KEY_CLIENT_ID
7. FIREBASE_SERVICE_ACCOUNT_KEY_AUTH_URI
8. FIREBASE_SERVICE_ACCOUNT_KEY_TOKEN_URI
9. FIREBASE_SERVICE_ACCOUNT_KEY_AUTH_PROVIDER_X509_CERT_URL
10. FIREBASE_SERVICE_ACCOUNT_KEY_CLIENT_X509_CERT_URL
11. FIREBASE_SERVICE_ACCOUNT_KEY_UNIVERSE_DOMAIN
12. CLOUDSQL_HOST
13. CLOUDSQL_NAME
14. CLOUDSQL_USER
15. CLOUDSQL_PASSWORD
16. WIF_PROVIDDER
17. WIF_SERVICE_ACCOUNT
18. ENVIRONMENT
19. BUCKET_NAME
20. DEBUG

Alternately, as you can see in `.github/workflows/deploy.yml`, there's an alternate option for authenticating Google Cloud for the deployment. In order to do that, set up the `GCP_CREDENTIALS` secret.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development purposes. See deployment for notes on how to deploy.
1. Create your own `.env` file in the root directory. Follow the environment format from `.env.example` file.
2. Create your virtual environment (venv), then open terminal at the root directory, activate your venv, and enter `~$ pip install -r requirements.txt`.
3. In terminal, enter `~$ python initialize.py` to initialize pre-configuration files.
4. Run `python manage.py runserver`

The server should be running on localhost:8000.

*Note that the `initialize.py` is not used in settings.py because it does pre-run things, such as generate configuration files, inject dependencies, etc.*

## Deployment
Follow the "Setting Up The Application" section above, then the application will be automatically deployed using GitHub Actions after each push/merge. Otherwise, can be altered if not using GitHub.
