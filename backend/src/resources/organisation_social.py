"""organisation_social.py

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
    from ..models import OrganisationSocialModel
    from ..utils.parse_params import parse_params
except ImportError:
    from models import OrganisationSocialModel
    from utils.parse_params import parse_params


class OrganisationSocialResource(Resource):
    """ The class is concern with the organisation social's CRUD API  """

    @staticmethod
    @parse_params(
        Argument("name", location="json", required=True,
                 help="The name of the organisation social."),
        Argument("link", location="json", required=True,
                 help="The link of the organisation social."),
        Argument("organisation", location="json", required=True,
                 help="The organisation id of the organisation social."),
    )
    def create(name, link, organisation):
        """ The function enables the creation of an organisation social"""

        try:
            new_organisation_social = OrganisationSocialModel(
                name=name,
                link=link,
                organisation=organisation,
            )
            new_organisation_social.save()

            return jsonify({
                'code': 201,
                'code_status': "created successfully",
                'data': {
                    'id': new_organisation_social.id,
                    'name': new_organisation_social.name,
                    'link': new_organisation_social.link,
                    'organisation': new_organisation_social.organisation,
                    'created_at': new_organisation_social.created_at,
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
        """ The function enables the reading of all organisation socials"""

        try:
            organisation_socials = OrganisationSocialModel.query.all()

            if not organisation_socials:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': "no organisation social found",
                }), 404

            organisation_socials_list = []

            for organisation_social in organisation_socials:
                organisation_socials_list.append({
                    'id': organisation_social.id,
                    'name': organisation_social.name,
                    'link': organisation_social.link,
                    'organisation': organisation_social.organisation,
                    'created_at': organisation_social.created_at,
                    'updated_at': organisation_social.updated_at,
                })

            return jsonify({
                'code': 200,
                'code_status': "retrieved successfully",
                'data': organisation_socials_list,
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
        """ The function enables the reading of one organisation social by id"""  # noqa

        try:
            organisation_social = OrganisationSocialModel.query.filter_by(
                id=id).first()

            if not organisation_social:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': f"no organisation social with id {id} was found",  # noqa
                }), 404

            return jsonify({
                'code': 200,
                'code_status': "retrieved successfully",
                'data': {
                    'id': organisation_social.id,
                    'name': organisation_social.name,
                    'link': organisation_social.link,
                    'organisation': organisation_social.organisation,
                    'created_at': organisation_social.created_at,
                    'updated_at': organisation_social.updated_at,
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
                 help="The name of the organisation social."),
        Argument("link", location="json",
                 help="The link of the organisation social."),
    )
    def update_one(id=None, **args):
        """ The function enables the updating of one organisation social by id"""  # noqa

        try:
            organisation_social = OrganisationSocialModel.query.filter_by(
                id=id).first()

            if not organisation_social:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': f"no organisation social with id {id} was found",  # noqa
                }), 404

            if 'name' in args and args['name'] is not None:
                organisation_social.name = args['name']

            if 'link' in args and args['link'] is not None:
                organisation_social.link = args['link']

            organisation_social.save()

            return jsonify({
                'code': 200,
                'code_status': "updated successfully",
                'data': {
                    'id': organisation_social.id,
                    'name': organisation_social.name,
                    'link': organisation_social.link,
                    'organisation': organisation_social.organisation,
                    'created_at': organisation_social.created_at,
                    'updated_at': organisation_social.updated_at,
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
        """ The function enables the deletion of one organisation social by id"""  # noqa

        try:
            organisation_social = OrganisationSocialModel.query.filter_by(
                id=id).first()

            if not organisation_social:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': f"no organisation social with id {id} was found",  # noqa
                }), 404

            organisation_social.delete()

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
