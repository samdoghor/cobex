"""organisational_role.py

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
    from ..models import OrganisationalRoleModel
    from ..utils.parse_params import parse_params
except ImportError:
    from models import OrganisationalRoleModel
    from utils.parse_params import parse_params


class OrganisationalRoleResource(Resource):
    """ The class is concern with the organisational role's CRUD API  """

    @staticmethod
    @parse_params(
        Argument("role", location="json", required=True,
                 help="The first name of the organisational role."),
        Argument("is_top_role", location="json", required=True, type=bool,
                 help="The last name of the organisational role."),
        Argument("is_member_role", location="json", required=True, type=bool,
                 help="The is_member role of the organisational role."),
        Argument("role_position", location="json", required=True,
                 help="The role position of the organisational role."),
        Argument("organisation", location="json", required=True,
                 help="The organisation the organisational role belong to."),
    )
    def create(role, is_top_role, is_member_role, role_position, organisation):
        """ The function enables the creation of an organisational role"""

        try:
            organisational_roles = OrganisationalRoleModel.query.filter_by(
                organisation=organisation).all()

            if organisational_roles is not None:
                for organisational_role in organisational_roles:
                    if organisational_role.is_top_role is True and organisational_role.role == "president":  # noqa
                        is_member_role = False
                        return jsonify({
                            'code': 409,
                            'code_status': "conflict",
                            'code_message': "a president is already existing",
                        }), 409

            new_organisational_role = OrganisationalRoleModel(
                role=role,
                is_top_role=is_top_role,
                is_member_role=is_member_role,
                role_position=role_position,
                organisation=organisation,
            )
            new_organisational_role.save()

            return jsonify({
                'code': 201,
                'code_status': "created successfully",
                'data': {
                    'id': new_organisational_role.id,
                    'role': new_organisational_role.role,
                    'is_top_role': new_organisational_role.is_top_role,
                    'is_member_role': new_organisational_role.is_member_role,
                    'role_position': new_organisational_role.role_position,
                    'organisation': new_organisational_role.organisation,
                    'created_at': new_organisational_role.created_at,
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
        """ The function enables the reading of all organisational roles"""

        try:
            organisational_roles = OrganisationalRoleModel.query.all()

            if not organisational_roles:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': "no organisational roles found",
                }), 404

            organisational_roles_list = []

            for organisational_role in organisational_roles:
                organisational_roles_list.append({
                    'id': organisational_role.id,
                    'role': organisational_role.role,
                    'is_top_role': organisational_role.is_top_role,
                    'is_member_role': organisational_role.is_member_role,
                    'role_position': organisational_role.role_position,
                    'created_at': organisational_role.created_at,
                    'updated_at': organisational_role.updated_at,
                    'organisation': organisational_role.organisation,
                })

            return jsonify({
                'code': 200,
                'code_status': "retrieved successfully",
                'data': organisational_roles_list,
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
        """ The function enables the reading of one organisational role by id"""  # noqa

        try:
            organisational_role = OrganisationalRoleModel.query.filter_by(
                id=id).first()

            if not organisational_role:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': f"no organisational role with id {id} was found",  # noqa
                }), 404

            return jsonify({
                'code': 200,
                'code_status': "retrieved successfully",
                'data': {
                    'id': organisational_role.id,
                    'role': organisational_role.role,
                    'is_top_role': organisational_role.is_top_role,
                    'is_member_role': organisational_role.is_member_role,
                    'role_position': organisational_role.role_position,
                    'created_at': organisational_role.created_at,
                    'updated_at': organisational_role.updated_at,
                    'organisation': organisational_role.organisation,
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
        Argument("role", location="json",
                 help="The first name of the organisational role."),
        Argument("is_top_role", location="json", type=bool,
                 help="The last name of the organisational role."),
        Argument("is_member_role", location="json", type=bool,
                 help="The is_member role of the organisational role."),
        Argument("role_position", location="json",
                 help="The role position of the organisational role."),
    )
    def update_one(id=None, **args):
        """ The function enables the updating of one organisational role by id"""  # noqa

        try:
            organisational_role = OrganisationalRoleModel.query.filter_by(
                id=id).first()

            if not organisational_role:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': f"no organisational role with id {id} was found",  # noqa
                }), 404

            if 'role' in args and args['role'] is not None:
                organisational_role.role = args['role']

            if 'is_top_role' in args and args['is_top_role'] is not None:
                organisational_role.is_top_role = args['is_top_role']

            if 'is_member_role' in args and args['is_member_role'] is not None:
                organisational_role.is_member_role = args['is_member_role']

            if 'role_position' in args and args['role_position'] is not None:
                organisational_role.role_position = args['role_position']

            organisational_role.save()

            return jsonify({
                'code': 200,
                'code_status': "updated successfully",
                'data': {
                    'id': organisational_role.id,
                    'role': organisational_role.role,
                    'is_top_role': organisational_role.is_top_role,
                    'is_member_role': organisational_role.is_member_role,
                    'role_position': organisational_role.role_position,
                    'created_at': organisational_role.created_at,
                    'updated_at': organisational_role.updated_at,
                    'organisation': organisational_role.organisation,
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
        """ The function enables the deletion of one organisational role by id"""  # noqa

        try:
            organisational_role = OrganisationalRoleModel.query.filter_by(id=id).first()  # noqa

            if not organisational_role:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': f"no organisational role with id {id} was found",  # noqa
                }), 404

            organisational_role.delete()

            return jsonify({
                'code': 200,
                'code_status': "deleted successfully",
                'code_message': f"{organisational_role.id} was deleted successfully",  # noqa
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
