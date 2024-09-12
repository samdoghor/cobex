"""organisational.py

Keyword arguments:
argument -- create, reall_all, read_one, update, delete
Return: create, reall_all, read_one, update, delete
"""

from flask import Blueprint

try:
    from ..resources import OrganisationResource
except ImportError:
    from resources import OrganisationResource


OrganisatonBlueprint = Blueprint("organisation", __name__)

OrganisatonBlueprint.route("/organisations",
                           methods=['POST'])(OrganisationResource.create)
OrganisatonBlueprint.route("/organisations",
                           methods=['GET'])(OrganisationResource.read_all)
OrganisatonBlueprint.route("/organisations/<uuid:id>",
                           methods=['GET'])(OrganisationResource.read_one)
OrganisatonBlueprint.route("/organisations/<uuid:id>",
                           methods=['PUT'])(OrganisationResource.update_one)
OrganisatonBlueprint.route("/organisations/<uuid:id>",
                           methods=['DELETE'])(OrganisationResource.delete_one)
