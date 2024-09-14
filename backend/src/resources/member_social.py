"""member_social.py

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
    from ..models import MemberSocialModel
    from ..utils.parse_params import parse_params
except ImportError:
    from models import MemberSocialModel
    from utils.parse_params import parse_params


class MemberSocialResource(Resource):
    """ The class is concern with the member social's CRUD API  """

    @staticmethod
    @parse_params(
        Argument("name", location="json", required=True,
                 help="The name of the member social."),
        Argument("link", location="json", required=True,
                 help="The link of the member social."),
        Argument("member", location="json", required=True,
                 help="The member id of the member social."),
    )
    def create(name, link, member):
        """ The function enables the creation of an member social"""

        try:
            new_member_social = MemberSocialModel(
                name=name,
                link=link,
                member=member,
            )
            new_member_social.save()

            return jsonify({
                'code': 201,
                'code_status': "created successfully",
                'data': {
                    'id': new_member_social.id,
                    'name': new_member_social.name,
                    'link': new_member_social.link,
                    'member': new_member_social.member,
                    'created_at': new_member_social.created_at,
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
        """ The function enables the reading of all member socials"""

        try:
            member_socials = MemberSocialModel.query.all()

            if not member_socials:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': "no member social found",
                }), 404

            member_socials_list = []

            for member_social in member_socials:
                member_socials_list.append({
                    'id': member_social.id,
                    'name': member_social.name,
                    'link': member_social.link,
                    'member': member_social.member,
                    'created_at': member_social.created_at,
                    'updated_at': member_social.updated_at,
                })

            return jsonify({
                'code': 200,
                'code_status': "retrieved successfully",
                'data': member_socials_list,
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
        """ The function enables the reading of one member social by id"""

        try:
            member_social = MemberSocialModel.query.filter_by(id=id).first()

            if not member_social:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': f"no member social with id {id} was found",
                }), 404

            return jsonify({
                'code': 200,
                'code_status': "retrieved successfully",
                'data': {
                    'id': member_social.id,
                    'name': member_social.name,
                    'link': member_social.link,
                    'member': member_social.member,
                    'created_at': member_social.created_at,
                    'updated_at': member_social.updated_at,
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
        Argument("name", location="json",
                 help="The name of the member social."),
        Argument("link", location="json",
                 help="The link of the member social."),
    )
    def update_one(id=None, **args):
        """ The function enables the updating of one member social by id"""

        try:
            member_social = MemberSocialModel.query.filter_by(id=id).first()

            if not member_social:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': f"no member social with id {id} was found",
                }), 404

            if 'name' in args and args['name'] is not None:
                member_social.name = args['name']

            if 'link' in args and args['link'] is not None:
                member_social.link = args['link']

            member_social.save()

            return jsonify({
                'code': 200,
                'code_status': "updated successfully",
                'data': {
                    'id': member_social.id,
                    'name': member_social.name,
                    'link': member_social.link,
                    'member': member_social.member,
                    'created_at': member_social.created_at,
                    'updated_at': member_social.updated_at,
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
        """ The function enables the deletion of one member social by id"""

        try:
            member_social = MemberSocialModel.query.filter_by(id=id).first()

            if not member_social:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': f"no member social with id {id} was found",
                }), 404

            member_social.delete()

            return jsonify({
                'code': 200,
                'code_status': "deleted successfully",
                'code_message': f"{id} was deleted"
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
