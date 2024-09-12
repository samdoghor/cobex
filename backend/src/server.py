"""server.py

Keyword arguments:
argument -- description
Return: flask_application
"""

from flask import Flask
from flask.blueprints import Blueprint
from flask_migrate import Migrate
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

Talisman(server)

server.config["SQLALCHEMY_DATABASE_URI"] = config.database_uri
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(server)
db.app = server
migrate = Migrate(server, db)

for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        server.register_blueprint(
            blueprint, url_prefix=config.application_api_root)

if __name__ == "__main__":
    server.run(host=config.application_host,
               port=config.application_port,
               debug=True if config.application_environment == "dev" else False)  # noqa
