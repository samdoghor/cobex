"""event.py

Keyword arguments:
argument -- create, reall_all, read_one, update, delete
Return: create, reall_all, read_one, update, delete
"""

from flask import Blueprint

try:
    from ..resources import MemberResource
except ImportError:
    from resources import MemberResource


MemberBlueprint = Blueprint("member", __name__)

MemberBlueprint.route("/members", methods=['POST'])(MemberResource.create)
MemberBlueprint.route("/members", methods=['GET'])(MemberResource.read_all)
MemberBlueprint.route("/members/<uuid:id>",
                      methods=['GET'])(MemberResource.read_one)
MemberBlueprint.route("/members/<uuid:id>",
                      methods=['PUT'])(MemberResource.update_one)
MemberBlueprint.route("/members/<uuid:id>",
                      methods=['DELETE'])(MemberResource.delete_one)
