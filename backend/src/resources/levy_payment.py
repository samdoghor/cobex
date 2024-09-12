"""levy_payment.py

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
    from ..models import LevyPaymentModel, OrganisationalLevyModel
    from ..utils.parse_params import parse_params
except ImportError:
    from models import LevyPaymentModel, OrganisationalLevyModel
    from utils.parse_params import parse_params


class LevyPaymentResource(Resource):
    """ The class is concern with the levy payment CRUD API  """

    @staticmethod
    @parse_params(
        Argument("amount", location="json", required=True,
                 help="The amount paid for the levy."),
        Argument("levy", location="json", required=True,
                 help="The levy the payment is slated for."),
        Argument("member", location="json", required=True,
                 help="The member who made the payment."),
        Argument("organisation", location="json", required=True,
                 help="The organisation the levy belong to."),
    )
    def create(amount, levy, member, organisation):
        """ The function enables the creation of a levy payment"""

        try:

            levy_id = OrganisationalLevyModel.query.filter_by(
                id=levy).first()

            all_levy_payment = LevyPaymentModel.query.all()

            if not levy_id:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': f"no levy id {levy} was found",
                }), 404

            if int(amount) != int(levy_id.amount):
                return jsonify({
                    'code': 404,
                    'code_status': "data mis-matched",
                    'code_message': "the amount you are inputting is wrong",
                }), 404

            reference = secrets.token_urlsafe(32)

            for levy_payment in all_levy_payment:
                while levy_payment.reference == reference:
                    reference = secrets.token_urlsafe(32)

                if str(levy_payment.member) == str(member) and str(
                        levy_payment.levy) == str(levy):
                    return jsonify({
                        'code': 409,
                        'code_status': "payment conflict",
                        'code_message': f"{member} has already made payment",
                    }), 409

            new_levy_payment = LevyPaymentModel(
                amount=amount,
                reference=reference,
                levy=levy,
                member=member,
                organisation=organisation,
            )
            new_levy_payment.save()

            return jsonify({
                'code': 201,
                'code_status': "created successfully",
                'data': {
                    'id': new_levy_payment.id,
                    'amount': new_levy_payment.amount,
                    'reference': new_levy_payment.reference,
                    'levy': new_levy_payment.levy,
                    'member': new_levy_payment.member,
                    'organisation': new_levy_payment.organisation,
                    'created_at': new_levy_payment.created_at,
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
        """ The function enables the reading of all levy payments"""

        try:
            levy_payments = LevyPaymentModel.query.all()

            if not levy_payments:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': "no levy payments found",
                }), 404

            levy_payments_list = []

            for levy_payment in levy_payments:
                levy_payments_list.append({
                    'id': levy_payment.id,
                    'amount': levy_payment.amount,
                    'reference': levy_payment.reference,
                    'created_at': levy_payment.created_at,
                    'updated_at': levy_payment.updated_at,
                    'levy': levy_payment.levy,
                    'member': levy_payment.member,
                    'organisation': levy_payment.organisation,
                })

            return jsonify({
                'code': 200,
                'code_status': "retrieved successfully",
                'data': levy_payments_list,
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
        """ The function enables the reading of one levy payment by id"""  # noqa

        try:
            levy_payment = LevyPaymentModel.query.filter_by(
                id=id).first()

            if not levy_payment:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': f"no levy payment with id {id} was found",  # noqa
                }), 404

            return jsonify({
                'code': 200,
                'code_status': "retrieved successfully",
                'data': {
                    'id': levy_payment.id,
                    'amount': levy_payment.amount,
                    'reference': levy_payment.reference,
                    'created_at': levy_payment.created_at,
                    'updated_at': levy_payment.updated_at,
                    'levy': levy_payment.levy,
                    'member': levy_payment.member,
                    'organisation': levy_payment.organisation,
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
        Argument("amount", location="json", required=True,
                 help="The amount paid for the levy."),
        Argument("reference", location="json", required=True,
                 help="The reference number for the payment."),
    )
    def update_one(id=None, **args):
        """ The function enables the updating of one levy payment by id"""  # noqa

        try:
            levy_payment = LevyPaymentModel.query.filter_by(
                id=id).first()

            if not levy_payment:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': f"no levy payment with id {id} was found",  # noqa
                }), 404

            if 'amount' in args and args['amount'] is not None:
                levy_payment.amount = args['amount']

            if 'reference' in args and args['reference'] is not None:
                levy_payment.reference = args['reference']

            levy_payment.save()

            return jsonify({
                'code': 200,
                'code_status': "updated successfully",
                'data': {
                    'id': levy_payment.id,
                    'amount': levy_payment.amount,
                    'reference': levy_payment.reference,
                    'created_at': levy_payment.created_at,
                    'updated_at': levy_payment.updated_at,
                    'levy': levy_payment.levy,
                    'member': levy_payment.member,
                    'organisation': levy_payment.organisation,
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
        """ The function enables the deletion of one levy payment by id"""  # noqa

        try:
            levy_payment = LevyPaymentModel.query.filter_by(id=id).first()  # noqa

            if not levy_payment:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': f"no levy payment with id {id} was found",  # noqa
                }), 404

            levy_payment.delete()

            return jsonify({
                'code': 200,
                'code_status': "deleted successfully",
                'code_message': f"{levy_payment.id} was deleted successfully",  # noqa
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
