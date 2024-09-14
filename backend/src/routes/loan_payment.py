"""loan_payment.py

Keyword arguments:
argument -- create, reall_all, read_one, delete
Return: create, reall_all, read_one, delete
"""

from flask import Blueprint

try:
    from ..resources import LoanPaymentResource
except ImportError:
    from resources import LoanPaymentResource


LoanPaymentBlueprint = Blueprint("loan_payment", __name__)

LoanPaymentBlueprint.route(
    "/loan-payments",
    methods=['POST'])(LoanPaymentResource.create)
LoanPaymentBlueprint.route(
    "/loan-payments",
    methods=['GET'])(LoanPaymentResource.read_all)
LoanPaymentBlueprint.route(
    "/loan-payments/<uuid:id>",
    methods=['GET'])(LoanPaymentResource.read_one)
LoanPaymentBlueprint.route(
    "/loan-payments/<uuid:id>",
    methods=['DELETE'])(LoanPaymentResource.delete_one)
