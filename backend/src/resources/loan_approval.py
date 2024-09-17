"""loan_approval.py

Keyword arguments:
argument -- description
Return: return_description
"""

from flask import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument
from sqlalchemy.exc import (DataError, IntegrityError, InterfaceError,
                            OperationalError, PendingRollbackError,
                            ProgrammingError)
from werkzeug.exceptions import BadRequest, MethodNotAllowed, NotFound

try:
    from ..models import LoanApprovalModel, LoanModel
    from ..utils.parse_params import parse_params
except ImportError:
    from models import LoanApprovalModel, LoanModel
    from utils.parse_params import parse_params


class LoanApprovalResource(Resource):
    """ The class is concern with the loan approval CRUD API  """

    @staticmethod
    @parse_params(
        Argument("loan", location="json", required=True,
                 help="The loan the payment is slated for."),
        Argument("member", location="json", required=True,
                 help="The member who approve the loan."),
        Argument("organisation", location="json", required=True,
                 help="The organisation the loan belong to."),
    )
    def create(loan, member, organisation):
        """ The function enables the creation of a loan approval"""

        try:

            loan_id = LoanModel.query.filter_by(
                id=loan).first()

            all_loan_approval = LoanApprovalModel.query.all()

            if not loan_id:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': f"no loan id {loan.id} was found",
                }), 404

            for loan_approval in all_loan_approval:

                if str(loan_approval.member) == str(member) and str(
                        loan_approval.loan) == str(loan):
                    return jsonify({
                        'code': 409,
                        'code_status': "approval conflict",
                        'code_message': f"{member} has already approve this loan",  # noqa
                    }), 409

            new_loan_approval = LoanApprovalModel(
                loan=loan,
                member=member,
                organisation=organisation
            )
            new_loan_approval.save()

            return jsonify({
                'code': 201,
                'code_status': "created successfully",
                'data': {
                    'id': new_loan_approval.id,
                    'loan': new_loan_approval.loan,
                    'member': new_loan_approval.member,
                    'organisation': new_loan_approval.organisation,
                    'created_at': new_loan_approval.created_at,
                }
            }), 201

        except IntegrityError:
            return jsonify({
                'code': 409,
                'code_status': "conflict",
                'code_message': "data is already existing",
            }), 409

        except (InterfaceError, OperationalError, PendingRollbackError,
                ProgrammingError):
            return jsonify({
                'code': 500,
                'code_status': "internal error",
                'code_message': "database connection error",
            }), 500

        except (DataError, NotFound):
            return jsonify({
                'code': 404,
                'code_status': "not found",
                'code_message': "data is missing or wrong",
            }), 404

        except BadRequest:
            return jsonify({
                'code': 400,
                'code_status': "bad request",
                'code_message': "input or datatype error",
            }), 400

        except MethodNotAllowed:
            return jsonify({
                'code': 405,
                'code_status': "method not allowed",
                'code_message': "improper url or method used",
            }), 405

    @staticmethod
    def read_all():
        """ The function enables the reading of all loan approvals"""

        try:
            loan_approvals = LoanApprovalModel.query.all()

            if not loan_approvals:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': "no loan approvals found",
                }), 404

            loan_approvals_list = []

            for loan_approval in loan_approvals:
                loan_approvals_list.append({
                    'id': loan_approval.id,
                    'created_at': loan_approval.created_at,
                    'updated_at': loan_approval.updated_at,
                    'loan': loan_approval.loan,
                    'member': loan_approval.member,
                    'organisation': loan_approval.organisation,
                })

            return jsonify({
                'code': 200,
                'code_status': "retrieved successfully",
                'data': loan_approvals_list,
            }), 200

        except (InterfaceError, OperationalError, PendingRollbackError,
                ProgrammingError):
            return jsonify({
                'code': 500,
                'code_status': "internal error",
                'code_message': "database connection error",
            }), 500

        except (DataError, NotFound):
            return jsonify({
                'code': 404,
                'code_status': "not found",
                'code_message': "data is missing or wrong",
            }), 404

        except MethodNotAllowed:
            return jsonify({
                'code': 405,
                'code_status': "method not allowed",
                'code_message': "improper url or method used",
            }), 405

    @staticmethod
    def read_one(id=None):
        """ The function enables the reading of one loan approval by id"""  # noqa

        try:
            loan_approval = LoanApprovalModel.query.filter_by(
                id=id).first()

            if not loan_approval:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': f"no loan approval with id {id} was found",  # noqa
                }), 404

            return jsonify({
                'code': 200,
                'code_status': "retrieved successfully",
                'data': {
                    'id': loan_approval.id,
                    'created_at': loan_approval.created_at,
                    'updated_at': loan_approval.updated_at,
                    'loan': loan_approval.loan,
                    'member': loan_approval.member,
                    'organisation': loan_approval.organisation,
                },
            }), 200

        except (InterfaceError, OperationalError, PendingRollbackError,
                ProgrammingError):
            return jsonify({
                'code': 500,
                'code_status': "internal error",
                'code_message': "database connection error",
            }), 500

        except (DataError, NotFound):
            return jsonify({
                'code': 404,
                'code_status': "not found",
                'code_message': "data is missing or wrong",
            }), 404

        except MethodNotAllowed:
            return jsonify({
                'code': 405,
                'code_status': "method not allowed",
                'code_message': "improper url or method used",
            }), 405

    @staticmethod
    def delete_one(id=None):
        """ The function enables the deletion of one loan approval by id"""  # noqa

        try:
            loan_approval = LoanApprovalModel.query.filter_by(id=id).first()  # noqa

            if not loan_approval:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': f"no loan approval with id {id} was found",  # noqa
                }), 404

            loan_approval.delete()

            return jsonify({
                'code': 200,
                'code_status': "deleted successfully",
                'code_message': f"{loan_approval.id} was deleted successfully",  # noqa
            }), 200

        except (InterfaceError, OperationalError, PendingRollbackError,
                ProgrammingError):
            return jsonify({
                'code': 500,
                'code_status': "internal error",
                'code_message': "database connection error",
            }), 500

        except (DataError, NotFound):
            return jsonify({
                'code': 404,
                'code_status': "not found",
                'code_message': "data is missing or wrong",
            }), 404

        except MethodNotAllowed:
            return jsonify({
                'code': 405,
                'code_status': "method not allowed",
                'code_message': "improper url or method used",
            }), 405
