"""levy_payment.py

Keyword arguments:
argument -- create, reall_all, read_one, update, delete
Return: create, reall_all, read_one, update, delete
"""

from flask import Blueprint

try:
    from ..resources import LevyPaymentResource
except ImportError:
    from resources import LevyPaymentResource


LevyPaymentBlueprint = Blueprint("levy_payment", __name__)

LevyPaymentBlueprint.route(
    "/levy-payments",
    methods=['POST'])(LevyPaymentResource.create)
LevyPaymentBlueprint.route(
    "/levy-payments",
    methods=['GET'])(LevyPaymentResource.read_all)
LevyPaymentBlueprint.route(
    "/levy-payments/<uuid:id>",
    methods=['GET'])(LevyPaymentResource.read_one)
LevyPaymentBlueprint.route(
    "/levy-payments/<uuid:id>",
    methods=['DELETE'])(LevyPaymentResource.delete_one)
