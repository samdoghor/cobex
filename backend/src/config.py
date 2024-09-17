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
application__client_path = os.getenv("CLIENT_PATH")

database_username = os.getenv("DATABASE_USERNAME")
database_passord = os.getenv("DATABASE_PASSWORD")
database_host = os.getenv("DATABASE_HOST")
database_name = os.getenv("DATABASE_NAME")
database_port = os.getenv("DATABASE_PORT")
database_uri = f"postgresql://{database_username}:{database_passord}@{database_host}:{database_port}/{database_name}"  # noqa

session_type = os.getenv("SESSION_TYPE")
session_permanent = os.getenv("SESSION_PERMANENT")
session_key_prefix = os.getenv("SESSION_KEY_PREFIX")
session_serialization_format = os.getenv("SESSION_SERIALIZATION_FORMAT")
session_sqlalchemy_table = os.getenv("SESSION_SQLALCHEMY_TABLE")
session_cleanup_n_requests = int(os.getenv("SESSION_CLEANUP_N_REQUESTS"))
session_cookie_name = os.getenv("SESSION_COOKIE_NAME")
session_cookie_httponly = os.getenv("SESSION_COOKIE_HTTPONLY")
session_cookie_secure = os.getenv("SESSION_COOKIE_SECURE")
session_cookie_samesite = os.getenv("SESSION_COOKIE_SAMESITE")
session_refresh_each_request = os.getenv("SESSION_REFRESH_EACH_REQUEST")
permanent_session_lifetime = int(os.getenv("PERMANENT_SESSION_LIFETIME"))

token_expiration = int(os.getenv("TOKEN_EXPIRATION"))
encryption_algorithm = os.getenv("ENCRYPTION_ALGORITHM")
