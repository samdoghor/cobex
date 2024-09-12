"""organisational_levy.py

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
    from ..models import OrganisationalLevyModel
    from ..utils.parse_params import parse_params
except ImportError:
    from models import OrganisationalLevyModel
    from utils.parse_params import parse_params


class OrganisationalLevyResource(Resource):
    """ The class is concern with the organisational levy's CRUD API  """

    @staticmethod
    @parse_params(
        Argument("levy_name", location="json", required=True,
                 help="The levy name."),
        Argument("interval", location="json", required=True,
                 help="The interval in which the levy will be collected."),
        Argument("amount", location="json", required=True,
                 help="The amount slated to be collected."),
        Argument("organisation", location="json", required=True,
                 help="The organisation the organisational role belong to."),
    )
    def create(levy_name, interval, amount, organisation):
        """ The function enables the creation of an member"""

        try:
            organisational_levy = OrganisationalLevyModel.query.filter_by(
                levy_name=levy_name).first()

            if organisational_levy:
                return jsonify({
                    'code': 409,
                    'code_status': "conflict",
                    'code_message': f"{levy_name} already exist",
                }), 409

            new_organisational_levy = OrganisationalLevyModel(
                levy_name=levy_name,
                interval=interval,
                amount=amount,
                organisation=organisation,
            )
            new_organisational_levy.save()

            return jsonify({
                'code': 201,
                'code_status': "created successfully",
                'data': {
                    'id': new_organisational_levy.id,
                    'levy_name': new_organisational_levy.levy_name,
                    'interval': new_organisational_levy.interval,
                    'amount': new_organisational_levy.amount,
                    'organisation': new_organisational_levy.organisation,
                    'created_at': new_organisational_levy.created_at,
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
        """ The function enables the reading of all organisational levies"""

        try:
            organisational_levies = OrganisationalLevyModel.query.all()

            if not organisational_levies:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': "no organisational levies found",
                }), 404

            organisational_levies_list = []

            for organisational_levy in organisational_levies:
                organisational_levies_list.append({
                    'id': organisational_levy.id,
                    'levy_name': organisational_levy.levy_name,
                    'interval': organisational_levy.interval,
                    'amount': organisational_levy.amount,
                    'created_at': organisational_levy.created_at,
                    'updated_at': organisational_levy.updated_at,
                    'organisation': organisational_levy.organisation,
                })

            return jsonify({
                'code': 200,
                'code_status': "retrieved successfully",
                'data': organisational_levies_list,
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
        """ The function enables the reading of one organisational levy by id"""  # noqa

        try:
            organisational_levy = OrganisationalLevyModel.query.filter_by(
                id=id).first()

            if not organisational_levy:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': f"no organisational levy with id {id} was found",  # noqa
                }), 404

            return jsonify({
                'code': 200,
                'code_status': "retrieved successfully",
                'data': {
                    'id': organisational_levy.id,
                    'levy_name': organisational_levy.levy_name,
                    'interval': organisational_levy.interval,
                    'amount': organisational_levy.amount,
                    'created_at': organisational_levy.created_at,
                    'updated_at': organisational_levy.updated_at,
                    'organisation': organisational_levy.organisation,
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
        Argument("levy_name", location="json",
                 help="The levy name."),
        Argument("interval", location="json",
                 help="The interval in which the levy will be collected."),
        Argument("amount", location="json",
                 help="The amount slated to be collected."),
    )
    def update_one(id=None, **args):
        """ The function enables the updating of one organisational levy by id"""  # noqa

        try:
            organisational_levy = OrganisationalLevyModel.query.filter_by(
                id=id).first()

            if not organisational_levy:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': f"no organisational levy with id {id} was found",  # noqa
                }), 404

            if 'levy_name' in args and args['levy_name'] is not None:
                organisational_levy.levy_name = args['levy_name']

            if 'interval' in args and args['interval'] is not None:
                organisational_levy.interval = args['interval']

            if 'amount' in args and args['amount'] is not None:
                organisational_levy.amount = args['amount']

            organisational_levy.save()

            return jsonify({
                'code': 200,
                'code_status': "updated successfully",
                'data': {
                    'id': organisational_levy.id,
                    'levy_name': organisational_levy.levy_name,
                    'interval': organisational_levy.interval,
                    'amount': organisational_levy.amount,
                    'created_at': organisational_levy.created_at,
                    'updated_at': organisational_levy.updated_at,
                    'organisation': organisational_levy.organisation,
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
        """ The function enables the deletion of one organisational levy by id"""  # noqa

        try:
            organisational_levy = OrganisationalLevyModel.query.filter_by(id=id).first()  # noqa

            if not organisational_levy:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': f"no organisational role with id {id} was found",  # noqa
                }), 404

            organisational_levy.delete()

            return jsonify({
                'code': 200,
                'code_status': "deleted successfully",
                'code_message': f"{organisational_levy.id} was deleted successfully",  # noqa
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
