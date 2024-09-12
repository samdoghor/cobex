"""loan.py

Keyword arguments:
argument -- create, reall_all, read_one, update, delete
Return: create, reall_all, read_one, update, delete
"""

from flask import Blueprint

try:
    from ..resources import LoanResource
except ImportError:
    from resources import LoanResource


LoanBlueprint = Blueprint("loan", __name__)

LoanBlueprint.route("/loans", methods=['POST'])(LoanResource.create)
LoanBlueprint.route("/loans", methods=['GET'])(LoanResource.read_all)
LoanBlueprint.route("/loans/<uuid:id>",
                    methods=['GET'])(LoanResource.read_one)
LoanBlueprint.route("/loans/<uuid:id>",
                    methods=['PUT'])(LoanResource.update_one)
LoanBlueprint.route("/loans/<uuid:id>",
                    methods=['DELETE'])(LoanResource.delete_one)
