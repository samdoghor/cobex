"""organisational_levy.py

Keyword arguments:
argument -- create, reall_all, read_one, update, delete
Return: create, reall_all, read_one, update, delete
"""

from flask import Blueprint

try:
    from ..resources import OrganisationalLevyResource
except ImportError:
    from resources import OrganisationalLevyResource


OrganisationalLevyBlueprint = Blueprint("organisational_levy", __name__)

OrganisationalLevyBlueprint.route(
    "/organisational-levies",
    methods=['POST'])(OrganisationalLevyResource.create)
OrganisationalLevyBlueprint.route(
    "/organisational-levies",
    methods=['GET'])(OrganisationalLevyResource.read_all)
OrganisationalLevyBlueprint.route(
    "/organisational-levies/<uuid:id>",
    methods=['GET'])(OrganisationalLevyResource.read_one)
OrganisationalLevyBlueprint.route(
    "/organisational-levies/<uuid:id>",
    methods=['PUT'])(OrganisationalLevyResource.update_one)
OrganisationalLevyBlueprint.route(
    "/organisational-levies/<uuid:id>",
    methods=['DELETE'])(OrganisationalLevyResource.delete_one)
