"""organisation_social.py

Keyword arguments:
argument -- create, reall_all, read_one, update, delete
Return: create, reall_all, read_one, update, delete
"""

from flask import Blueprint

try:
    from ..resources import OrganisationSocialResource
except ImportError:
    from resources import OrganisationSocialResource


OrganisationSocialBlueprint = Blueprint("organisation_social", __name__)

OrganisationSocialBlueprint.route(
    "/organisation-socials",
    methods=['POST'])(OrganisationSocialResource.create)
OrganisationSocialBlueprint.route(
    "/organisation-socials",
    methods=['GET'])(OrganisationSocialResource.read_all)
OrganisationSocialBlueprint.route(
    "/organisation-socials/<uuid:id>",
    methods=['GET'])(OrganisationSocialResource.read_one)
OrganisationSocialBlueprint.route(
    "/organisation-socials/<uuid:id>",
    methods=['PUT'])(OrganisationSocialResource.update_one)
OrganisationSocialBlueprint.route(
    "/organisation-socials/<uuid:id>",
    methods=['DELETE'])(OrganisationSocialResource.delete_one)
