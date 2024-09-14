"""organisation_account.py

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
    from ..models import OrganisationAccountModel
    from ..utils.parse_params import parse_params
except ImportError:
    from models import OrganisationAccountModel
    from utils.parse_params import parse_params


class OrganisationAccountResource(Resource):
    """ The class is concern with the organisation account's CRUD API  """

    @staticmethod
    @parse_params(
        Argument("bank_name", location="json", required=True,
                 help="The bank name of the organisation."),
        Argument("bank_code", location="json", required=True,
                 help="The bank code of the organisation."),
        Argument("account_name", location="json", required=True,
                 help="The account name of the organisation."),
        Argument("account_number", location="json", required=True,
                 help="The role account number of the organisation."),
        Argument("organisation", location="json", required=True,
                 help="The organisation of whick the account belong to."),
    )
    def create(bank_name, bank_code, account_name, account_number,
               organisation):
        """ The function enables the creation of an organisation account"""

        try:
            organisation_account = OrganisationAccountModel.query.filter_by(account_number=account_number, organisation=organisation).first()  # noqa

            all_organisation_account = OrganisationAccountModel.query.filter_by(organisation=organisation).all()  # noqa

            if len(account_number) < 10:
                return jsonify({
                    'code': 400,
                    'code_status': "bad request",
                    'code_message': f"{account_number} is less than expect numbers",  # noqa
                }), 400

            if len(account_number) > 10:
                return jsonify({
                    'code': 400,
                    'code_status': "bad request",
                    'code_message': f"{account_number} is greater than expect numbers",  # noqa
                }), 400

            if organisation_account:
                return jsonify({
                    'code': 409,
                    'code_status': "conflict",
                    'code_message': f"{account_number} already exist",
                }), 409

            if len(all_organisation_account) >= 3:
                return jsonify({
                    'code': 409,
                    'code_status': "conflict",
                    'code_message': "can not exceed more than 3 bank account",
                }), 409

            new_organisation_account = OrganisationAccountModel(
                bank_name=bank_name,
                bank_code=bank_code,
                account_name=account_name,
                account_number=account_number,
                organisation=organisation,
            )
            new_organisation_account.save()

            return jsonify({
                'code': 201,
                'code_status': "created successfully",
                'data': {
                    'id': new_organisation_account.id,
                    'bank_name': new_organisation_account.bank_name,
                    'bank_code': new_organisation_account.bank_code,
                    'account_name': new_organisation_account.account_name,
                    'account_number': new_organisation_account.account_number,  # noqa
                    'organisation': new_organisation_account.organisation,
                    'created_at': new_organisation_account.created_at,
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
        """ The function enables the reading of all organisation accounts"""

        try:
            organisation_accounts = OrganisationAccountModel.query.all()

            if not organisation_accounts:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': "no organisation accounts found",
                }), 404

            organisation_accounts_list = []

            for organisation_account in organisation_accounts:
                organisation_accounts_list.append({
                    'id': organisation_account.id,
                    'bank_name': organisation_account.bank_name,
                    'bank_code': organisation_account.bank_code,
                    'account_name': organisation_account.account_name,
                    'account_number': organisation_account.account_number,  # noqa
                    'created_at': organisation_account.created_at,
                    'updated_at': organisation_account.updated_at,
                    'organisation': organisation_account.organisation,
                })

            return jsonify({
                'code': 200,
                'code_status': "retrieved successfully",
                'data': organisation_accounts_list,
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
        """ The function enables the reading of one organisation account by id"""  # noqa

        try:
            organisation_account = OrganisationAccountModel.query.filter_by(id=id).first()  # noqa

            if not organisation_account:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': f"no organisation account with id {id} was found",  # noqa
                }), 404

            return jsonify({
                'code': 200,
                'code_status': "retrieved successfully",
                'data': {
                    'id': organisation_account.id,
                    'bank_name': organisation_account.bank_name,
                    'bank_code': organisation_account.bank_code,
                    'account_name': organisation_account.account_name,
                    'account_number': organisation_account.account_number,  # noqa
                    'created_at': organisation_account.created_at,
                    'updated_at': organisation_account.updated_at,
                    'organisation': organisation_account.organisation,
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
        Argument("bank_name", location="json",
                 help="The bank name of the organisation."),
        Argument("bank_code", location="json",
                 help="The bank code of the organisation."),
        Argument("account_name", location="json",
                 help="The account name of the organisation."),
        Argument("account_number", location="json",
                 help="The role account number of the organisation."),
    )
    def update_one(id=None, **args):
        """ The function enables the updating of one organisation account by id"""  # noqa

        try:
            organisation_account = OrganisationAccountModel.query.filter_by(id=id).first()  # noqa

            if not organisation_account:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': f"no organisation account with id {id} was found",  # noqa
                }), 404

            if 'bank_name' in args and args['bank_name'] is not None:
                organisation_account.bank_name = args['bank_name']

            if 'bank_code' in args and args['bank_code'] is not None:
                organisation_account.bank_code = args['bank_code']

            if 'account_name' in args and args['account_name'] is not None:
                organisation_account.account_name = args['account_name']

            if 'account_number' in args and args['account_number'] is not None:
                organisation_account.account_number = args['account_number']

            organisation_account.save()

            return jsonify({
                'code': 200,
                'code_status': "updated successfully",
                'data': {
                    'id': organisation_account.id,
                    'bank_name': organisation_account.bank_name,
                    'bank_code': organisation_account.bank_code,
                    'account_name': organisation_account.account_name,
                    'account_number': organisation_account.account_number,  # noqa
                    'created_at': organisation_account.created_at,
                    'updated_at': organisation_account.updated_at,
                    'organisation': organisation_account.organisation,
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
        """ The function enables the deletion of one organisation account by id"""  # noqa

        try:
            organisation_account = OrganisationAccountModel.query.filter_by(id=id).first()  # noqa

            if not organisation_account:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': f"no organisation account with id {id} was found",  # noqa
                }), 404

            organisation_account.delete()

            return jsonify({
                'code': 200,
                'code_status': "deleted successfully",
                'code_message': f"{organisation_account.id} was deleted successfully",  # noqa
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
