"""organisational_role.py

Keyword arguments:
argument -- create, reall_all, read_one, update, delete
Return: create, reall_all, read_one, update, delete
"""

from flask import Blueprint

try:
    from ..resources import OrganisationalRoleResource
except ImportError:
    from resources import OrganisationalRoleResource


OrganisationalRoleBlueprint = Blueprint("organisational_role", __name__)

OrganisationalRoleBlueprint.route(
    "/organisational-roles",
    methods=['POST'])(OrganisationalRoleResource.create)
OrganisationalRoleBlueprint.route(
    "/organisational-roles",
    methods=['GET'])(OrganisationalRoleResource.read_all)
OrganisationalRoleBlueprint.route(
    "/organisational-roles/<uuid:id>",
    methods=['GET'])(OrganisationalRoleResource.read_one)
OrganisationalRoleBlueprint.route(
    "/organisational-roles/<uuid:id>",
    methods=['PUT'])(OrganisationalRoleResource.update_one)
OrganisationalRoleBlueprint.route(
    "/organisational-roles/<uuid:id>",
    methods=['DELETE'])(OrganisationalRoleResource.delete_one)
