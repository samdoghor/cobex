"""config.py

Keyword arguments:
argument -- description
Return: environment_variables
"""

import os

from dotenv import load_dotenv

load_dotenv()

application_secret_key = os.getenv("SECRET_KEY")
application_environment = os.getenv("ENVIRONMENT")

application_host = os.getenv("APPLICATION_HOST")
application_port = os.getenv("APPLICATION_PORT")
application_api_root = os.getenv("API_ROOT")
application__api_path = os.getenv("API_PATH")

database_username = os.getenv("DATABASE_USERNAME")
database_passord = os.getenv("DATABASE_PASSWORD")
database_host = os.getenv("DATABASE_HOST")
database_name = os.getenv("DATABASE_NAME")
database_port = os.getenv("DATABASE_PORT")
database_uri = f"postgresql://{database_username}:{database_passord}@{database_host}:{database_port}/{database_name}"  # noqa
