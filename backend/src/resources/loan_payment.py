"""loan_payment.py

Keyword arguments:
argument -- description
Return: return_description
"""

import secrets

from flask import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument
from sqlalchemy.exc import (DataError, IntegrityError, InterfaceError,
                            OperationalError, PendingRollbackError,
                            ProgrammingError)
from werkzeug.exceptions import BadRequest, MethodNotAllowed, NotFound

try:
    from ..models import LoanPaymentModel, LoanModel
    from ..utils.parse_params import parse_params
except ImportError:
    from models import LoanPaymentModel, LoanModel
    from utils.parse_params import parse_params


class LoanPaymentResource(Resource):
    """ The class is concern with the loan payment CRUD API  """

    @staticmethod
    @parse_params(
        Argument("amount", location="json", required=True,
                 help="The amount paid for the loan."),
        Argument("loan", location="json", required=True,
                 help="The loan the payment is slated for."),
        Argument("member", location="json", required=True,
                 help="The member who made the payment."),
        Argument("organisation", location="json", required=True,
                 help="The organisation the loan belong to."),
    )
    def create(amount, loan, member, organisation):
        """ The function enables the creation of a loan payment"""

        try:

            loan_id = LoanModel.query.filter_by(
                id=loan).first()

            all_loan_payment = LoanPaymentModel.query.all()

            user_loan_payment = LoanPaymentModel.query.filter_by(
                loan=loan, member=member).all()

            if not loan_id:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': f"no loan id {loan} was found",
                }), 404

            reference = secrets.token_urlsafe(32)

            loan_owed = loan_id.total_amount
            amount_paid = 0

            for one_payment in user_loan_payment:
                amount_paid += int(one_payment.amount)

            for loan_payment in all_loan_payment:
                while loan_payment.reference == reference:
                    reference = secrets.token_urlsafe(32)

            prev_loan_balance = loan_owed - amount_paid

            if prev_loan_balance == 0:
                return jsonify({
                    'code': 409,
                    'code_status': "payment conflict",
                    'code_message': "no loan balance, payment complete"
                }), 409

            if float(amount) > prev_loan_balance:
                return jsonify({
                    'code': 409,
                    'code_status': "payment conflict",
                    'code_message': f"{amount} too big, pay {prev_loan_balance}"  # noqa
                }), 409

            new_loan_payment = LoanPaymentModel(
                amount=amount,
                reference=reference,
                loan=loan,
                member=member,
                organisation=organisation,
            )
            new_loan_payment.save()

            new_loan_balance = prev_loan_balance - new_loan_payment.amount

            return jsonify({
                'code': 201,
                'code_status': "created successfully",
                'data': {
                    'id': new_loan_payment.id,
                    'amount': new_loan_payment.amount,
                    'reference': new_loan_payment.reference,
                    'loan': new_loan_payment.loan,
                    'member': new_loan_payment.member,
                    'loan_balance': new_loan_balance,
                    'organisation': new_loan_payment.organisation,
                    'created_at': new_loan_payment.created_at,
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
        """ The function enables the reading of all loan payments"""

        try:
            loan_payments = LoanPaymentModel.query.all()

            if not loan_payments:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': "no loan payments found",
                }), 404

            loan_payments_list = []

            for loan_payment in loan_payments:
                loan_payments_list.append({
                    'id': loan_payment.id,
                    'amount': loan_payment.amount,
                    'reference': loan_payment.reference,
                    'created_at': loan_payment.created_at,
                    'updated_at': loan_payment.updated_at,
                    'loan': loan_payment.loan,
                    'member': loan_payment.member,
                    'organisation': loan_payment.organisation,
                })

            return jsonify({
                'code': 200,
                'code_status': "retrieved successfully",
                'data': loan_payments_list,
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
        """ The function enables the reading of one loan payment by id"""  # noqa

        try:
            loan_payment = LoanPaymentModel.query.filter_by(
                id=id).first()

            if not loan_payment:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': f"no loan payment with id {id} was found",  # noqa
                }), 404

            return jsonify({
                'code': 200,
                'code_status': "retrieved successfully",
                'data': {
                    'id': loan_payment.id,
                    'amount': loan_payment.amount,
                    'reference': loan_payment.reference,
                    'created_at': loan_payment.created_at,
                    'updated_at': loan_payment.updated_at,
                    'loan': loan_payment.loan,
                    'member': loan_payment.member,
                    'organisation': loan_payment.organisation,
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

    @ staticmethod
    def delete_one(id=None):
        """ The function enables the deletion of one loan payment by id"""  # noqa

        try:
            loan_payment = LoanPaymentModel.query.filter_by(id=id).first()  # noqa

            if not loan_payment:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': f"no loan payment with id {id} was found",  # noqa
                }), 404

            loan_payment.delete()

            return jsonify({
                'code': 200,
                'code_status': "deleted successfully",
                'code_message': f"{loan_payment.id} was deleted successfully",  # noqa
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
