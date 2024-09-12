"""loan.py

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
    from ..models import LoanModel
    from ..utils.parse_params import parse_params
except ImportError:
    from models import LoanModel
    from utils.parse_params import parse_params


class LoanResource(Resource):
    """ The class is concern with the lona's CRUD API  """

    @staticmethod
    @parse_params(
        Argument("amount", location="json", required=True,
                 help="The amount paid for the loan."),
        Argument("due_date", location="json", required=True,
                 help="The due date for the loan."),
        Argument("interest_at", location="json", required=True,
                 help="The interest rate for the loan."),
        Argument("member", location="json", required=True,
                 help="The member who made the loan request."),
        Argument("organisation", location="json", required=True,
                 help="The organisation the loan belong to."),
    )
    def create(amount, due_date, interest_at, member, organisation):
        """ The function enables the creation of a laon"""

        try:

            interest_amount = int(amount) * float(interest_at)/100
            total_amount = int(amount) + float(interest_amount)

            new_loan = LoanModel(
                amount=amount,
                due_date=due_date,
                interest_at=interest_at,
                interest_amount=interest_amount,
                total_amount=total_amount,
                member=member,
                organisation=organisation,
            )
            new_loan.save()

            return jsonify({
                'code': 201,
                'code_status': "created successfully",
                'data': {
                    'id': new_loan.id,
                    'amount': new_loan.amount,
                    'due_date': new_loan.due_date,
                    'interest_at': new_loan.interest_at,
                    'interest_amount': new_loan.interest_amount,
                    'total_amount': new_loan.total_amount,
                    'member': new_loan.member,
                    'organisation': new_loan.organisation,
                    'created_at': new_loan.created_at,
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
        """ The function enables the reading of all loans"""

        try:
            loans = LoanModel.query.all()

            if not loans:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': "no loans found",
                }), 404

            loan_list = []

            for loan in loans:
                loan_list.append({
                    'id': loan.id,
                    'amount': loan.amount,
                    'due_date': loan.due_date,
                    'interest_at': loan.interest_at,
                    'interest_amount': loan.interest_amount,
                    'total_amount': loan.total_amount,
                    'member': loan.member,
                    'organisation': loan.organisation,
                    'created_at': loan.created_at,
                    'updated_at': loan.updated_at,
                })

            return jsonify({
                'code': 200,
                'code_status': "retrieved successfully",
                'data': loan_list,
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
        """ The function enables the reading of one loan by id"""  # noqa

        try:
            loan = LoanModel.query.filter_by(
                id=id).first()

            if not loan:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': f"no loan with id {id} was found",  # noqa
                }), 404

            return jsonify({
                'code': 200,
                'code_status': "retrieved successfully",
                'data': {
                    'id': loan.id,
                    'amount': loan.amount,
                    'due_date': loan.due_date,
                    'interest_at': loan.interest_at,
                    'interest_amount': loan.interest_amount,
                    'total_amount': loan.total_amount,
                    'member': loan.member,
                    'organisation': loan.organisation,
                    'created_at': loan.created_at,
                    'updated_at': loan.updated_at,
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
    @parse_params(
        Argument("amount", location="json",
                 help="The amount paid for the loan."),
        Argument("due_date", location="json",
                 help="The due date for the loan."),
        Argument("interest_at", location="json",
                 help="The interest rate for the loan."),
    )
    def update_one(id=None, **args):
        """ The function enables the updating of one loan by id"""  # noqa

        try:
            loan = LoanModel.query.filter_by(
                id=id).first()

            if not loan:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': f"no loan with id {id} was found",  # noqa
                }), 404

            if 'amount' in args and args['amount'] is not None:
                loan.amount = args['amount']
                loan.interest_amount = int(args['amount']) * float(loan.interest_at)/100  # noqa
                loan.total_amount = int(args['amount']) + float(loan.interest_amount)  # noqa

            if 'due_date' in args and args['due_date'] is not None:
                loan.due_date = args['due_date']

            if 'interest_at' in args and args['interest_at'] is not None:
                loan.interest_at = args['interest_at']
                loan.interest_amount = int(loan.amount) * float(args['interest_at'])/100  # noqa
                loan.total_amount = int(loan.amount) + float(loan.interest_amount)  # noqa

            loan.save()

            return jsonify({
                'code': 200,
                'code_status': "updated successfully",
                'data': {
                    'id': loan.id,
                    'amount': loan.amount,
                    'due_date': loan.due_date,
                    'interest_at': loan.interest_at,
                    'interest_amount': loan.interest_amount,
                    'total_amount': loan.total_amount,
                    'member': loan.member,
                    'organisation': loan.organisation,
                    'created_at': loan.created_at,
                    'updated_at': loan.updated_at,
                }
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

    @ staticmethod
    def delete_one(id=None):
        """ The function enables the deletion of one loan by id"""  # noqa

        try:
            loan = LoanModel.query.filter_by(id=id).first()

            if not loan:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': f"no loan with id {id} was found",  # noqa
                }), 404

            loan.delete()

            return jsonify({
                'code': 200,
                'code_status': "deleted successfully",
                'code_message': f"{loan.id} was deleted successfully",
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
