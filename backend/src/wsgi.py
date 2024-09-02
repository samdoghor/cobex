"""wsgi.py

Keyword arguments:
argument -- description
Return: wsgi_server
"""

try:
    from . import config
    from .server import server as cobex
except ImportError:
    import config
    from server import server as cobex


if __name__ == "__main__":
    if config.application_env == "prod":
        cobex.run()
