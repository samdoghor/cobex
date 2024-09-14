"""member_social.py

Keyword arguments:
argument -- create, reall_all, read_one, update, delete
Return: create, reall_all, read_one, update, delete
"""

from flask import Blueprint

try:
    from ..resources import MemberSocialResource
except ImportError:
    from resources import MemberSocialResource


MemberSocialBlueprint = Blueprint("member_social", __name__)

MemberSocialBlueprint.route(
    "/member-socials",
    methods=['POST'])(MemberSocialResource.create)
MemberSocialBlueprint.route(
    "/member-socials",
    methods=['GET'])(MemberSocialResource.read_all)
MemberSocialBlueprint.route(
    "/member-socials/<uuid:id>",
    methods=['GET'])(MemberSocialResource.read_one)
MemberSocialBlueprint.route(
    "/member-socials/<uuid:id>",
    methods=['PUT'])(MemberSocialResource.update_one)
MemberSocialBlueprint.route(
    "/member-socials/<uuid:id>",
    methods=['DELETE'])(MemberSocialResource.delete_one)
