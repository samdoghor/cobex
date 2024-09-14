"""authentication.py

Keyword arguments:
argument -- create, reall_all, read_one, update, delete
Return: create, reall_all, read_one, update, delete
"""

from flask import Blueprint

try:
    from ..resources import AuthenticationResource
except ImportError:
    from resources import AuthenticationResource


AuthenticationBlueprint = Blueprint("authentication", __name__)

AuthenticationBlueprint.route(
    "/auth/login", methods=['POST'])(AuthenticationResource.login)

AuthenticationBlueprint.route(
    "/auth/logout", methods=['POST'])(AuthenticationResource.logout)
