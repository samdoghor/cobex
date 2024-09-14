"""organisation_account.py

Keyword arguments:
argument -- create, reall_all, read_one, update, delete
Return: create, reall_all, read_one, update, delete
"""

from flask import Blueprint

try:
    from ..resources import OrganisationAccountResource
except ImportError:
    from resources import OrganisationAccountResource


OrganisationAccountBlueprint = Blueprint("organisation_account", __name__)

OrganisationAccountBlueprint.route(
    "/organisation-accounts",
    methods=['POST'])(OrganisationAccountResource.create)
OrganisationAccountBlueprint.route(
    "/organisation-accounts",
    methods=['GET'])(OrganisationAccountResource.read_all)
OrganisationAccountBlueprint.route(
    "/organisation-accounts/<uuid:id>",
    methods=['GET'])(OrganisationAccountResource.read_one)
OrganisationAccountBlueprint.route(
    "/organisation-accounts/<uuid:id>",
    methods=['PUT'])(OrganisationAccountResource.update_one)
OrganisationAccountBlueprint.route(
    "/organisation-accounts/<uuid:id>",
    methods=['DELETE'])(OrganisationAccountResource.delete_one)
