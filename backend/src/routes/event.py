"""event.py

Keyword arguments:
argument -- create, reall_all, read_one, update, delete
Return: create, reall_all, read_one, update, delete
"""

from flask import Blueprint

try:
    from ..resources import EventResource
except ImportError:
    from resources import EventResource


EventBlueprint = Blueprint("event", __name__)

EventBlueprint.route("/events", methods=['POST'])(EventResource.create)
EventBlueprint.route("/events", methods=['GET'])(EventResource.read_all)
EventBlueprint.route("/events/<uuid:id>",
                     methods=['GET'])(EventResource.read_one)
EventBlueprint.route("/events/<uuid:id>",
                     methods=['PUT'])(EventResource.update_one)
EventBlueprint.route("/events/<uuid:id>",
                     methods=['DELETE'])(EventResource.delete_one)
