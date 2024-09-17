"""server.py

Keyword arguments:
argument -- description
Return: flask_application
"""

from flask import Flask
from flask.blueprints import Blueprint
from flask_cors import CORS
from flask_migrate import Migrate
from flask_session import Session
from flask_talisman import Talisman

try:
    from . import config, routes
    from .models import db
except ImportError:
    import config
    import routes
    from models import db


server = Flask(__name__)
server.secret_key = config.application_secret_key

server.config['SESSION_TYPE'] = config.session_type
server.config['SESSION_PERMANENT'] = config.session_permanent
server.config['SESSION_KEY_PREFIX'] = config.session_key_prefix
server.config['SESSION_SERIALIZATION_FORMAT'] = config.session_serialization_format  # noqa
server.config['SESSION_SQLALCHEMY'] = db
server.config['SESSION_SQLALCHEMY_TABLE'] = config.session_sqlalchemy_table
server.config['SESSION_CLEANUP_N_REQUESTS'] = config.session_cleanup_n_requests
server.config['SESSION_COOKIE_NAME'] = config.session_cookie_name
server.config['SESSION_COOKIE_DOMAIN'] = config.application__client_path
server.config['SESSION_COOKIE_PATH'] = config.application_api_root
server.config['SESSION_COOKIE_HTTPONLY'] = config.session_cookie_httponly
server.config['SESSION_COOKIE_SECURE'] = config.session_cookie_secure
server.config['SESSION_COOKIE_SAMESITE'] = config.session_cookie_samesite
server.config['SESSION_REFRESH_EACH_REQUEST'] = config.session_refresh_each_request  # noqa
server.config['PERMANENT_SESSION_LIFETIME'] = config.permanent_session_lifetime
server.config.from_object(__name__)

Talisman(server)

allowed_origins = [
    config.application__client_path
]

cors = CORS(server,
            resources={r"/api-cobex/*": {"origins": allowed_origins}},
            methods=["POST", "GET", "PUT", "DELETE"],
            allow_headers=["Authorization", "Content-Type"],
            supports_credentials=True,
            max_age=3600)

server.config["SQLALCHEMY_DATABASE_URI"] = config.database_uri
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(server)
db.app = server
migrate = Migrate(server, db)

Session(server)

for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        server.register_blueprint(
            blueprint, url_prefix=config.application_api_root)

if __name__ == "__main__":
    server.run(host=config.application_host,
               port=config.application_port,
               debug=True if config.application_environment == "dev" else False)  # noqa
