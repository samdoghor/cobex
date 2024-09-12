"""loan_approval.py

Keyword arguments:
argument -- create, reall_all, read_one, update, delete
Return: create, reall_all, read_one, update, delete
"""

from flask import Blueprint

try:
    from ..resources import LoanApprovalResource
except ImportError:
    from resources import LoanApprovalResource


LoanApprovalBlueprint = Blueprint("loan-approval", __name__)

LoanApprovalBlueprint.route(
    "/loan-approvals", methods=['POST'])(LoanApprovalResource.create)
LoanApprovalBlueprint.route(
    "/loan-approvals", methods=['GET'])(LoanApprovalResource.read_all)
LoanApprovalBlueprint.route("/loan-approvals/<uuid:id>",
                            methods=['GET'])(LoanApprovalResource.read_one)
LoanApprovalBlueprint.route(
    "/loan-approvals/<uuid:id>",
    methods=['DELETE'])(LoanApprovalResource.delete_one)
