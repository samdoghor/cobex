"""organisation.py

Keyword arguments:
argument -- description
Return: return_description
"""
import secrets
# from datetime import timedelta
from flask import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument
from sqlalchemy.exc import (DataError, IntegrityError, InterfaceError,
                            OperationalError, PendingRollbackError,
                            ProgrammingError)
from werkzeug.exceptions import BadRequest, MethodNotAllowed, NotFound

try:
    from ..models import OrganisationModel, MemberModel
    from ..utils.parse_params import parse_params
    # from ..utils import NetworkTime
except ImportError:
    from models import OrganisationModel, MemberModel
    from utils.parse_params import parse_params
    # from utils import NetworkTime


class OrganisationResource(Resource):
    """ The class is concern with the organisation's CRUD API  """

    @staticmethod
    @parse_params(
        Argument("full_name", location="json", required=True,
                 help="The full name of the organisation."),
        Argument("email", location="json", required=True,
                 help="The email of the organisation."),
    )
    def create(full_name, email):
        """ The function enables the creation of an organisation"""

        try:
            organisation = OrganisationModel.query.filter_by(
                email=email).first()

            organisations = OrganisationModel.query.all()

            member = MemberModel.query.filter_by(
                email=email).first()

            if organisation is not None:
                return jsonify({
                    'code': 409,
                    'code_status': "conflict",
                    'code_message': f"{email} already has an account",
                }), 409

            if member is not None:
                return jsonify({
                    'code': 409,
                    'code_status': "conflict",
                    'code_message': f"{email} was used for a member account",
                }), 409

            username = secrets.token_urlsafe(8)

            for organisation in organisations:
                while organisation.username == username:
                    username = secrets.token_urlsafe(8)

            new_organisation = OrganisationModel(
                full_name=full_name,
                email=email,
                username=username,
            )
            new_organisation.save()

            return jsonify({
                'code': 201,
                'code_status': "created successfully",
                'data': {
                    'id': new_organisation.id,
                    'full_name': new_organisation.full_name,
                    'email': new_organisation.email,
                    'username': new_organisation.username,
                    'is_hq': new_organisation.is_hq,
                    'is_incorporated': new_organisation.is_incorporated,
                    'verified': new_organisation.verified,
                    'setup_completed': new_organisation.setup_completed,
                    'created_at': new_organisation.created_at,
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
        """ The function enables the reading of all organisations"""

        try:
            organisations = OrganisationModel.query.all()

            if not organisations:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': "no organisation found",
                }), 404

            organisations_list = []

            for organisation in organisations:
                organisations_list.append({
                    'id': organisation.id,
                    'full_name': organisation.full_name,
                    'email': organisation.email,
                    'date_of_establishment': organisation.date_of_establishment,  # noqa
                    'country': organisation.country,
                    'state': organisation.state,
                    'city': organisation.city,
                    'address': organisation.address,
                    'postal_code': organisation.postal_code,
                    'is_hq': organisation.is_hq,
                    'hq_id': organisation.hq_id,
                    'is_incorporated': organisation.is_incorporated,
                    'date_of_incorporation': organisation.date_of_incorporation,  # noqa
                    'legal_name': organisation.legal_name,
                    'logo': organisation.logo,
                    'logo_id': organisation.logo_id,
                    'banner': organisation.banner,
                    'banner_id': organisation.banner_id,
                    'slogan': organisation.slogan,
                    'phone': organisation.phone,
                    'website': organisation.website,
                    'description': organisation.description,
                    'username': organisation.username,
                    'verified': organisation.verified,
                    'setup_completed': organisation.setup_completed,
                    'can_loan': organisation.can_loan,
                    'created_at': organisation.created_at,
                    'updated_at': organisation.updated_at,
                })

            return jsonify({
                'code': 200,
                'code_status': "retrieved successfully",
                'data': organisations_list,
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
        """ The function enables the reading of one organisation by id"""

        try:
            organisation = OrganisationModel.query.filter_by(id=id).first()

            if not organisation:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': f"no organisation with id {id} was found",
                }), 404

            return jsonify({
                'code': 200,
                'code_status': "retrieved successfully",
                'data': {
                    'id': organisation.id,
                    'full_name': organisation.full_name,
                    'email': organisation.email,
                    'date_of_establishment': organisation.date_of_establishment,  # noqa
                    'country': organisation.country,
                    'state': organisation.state,
                    'city': organisation.city,
                    'address': organisation.address,
                    'postal_code': organisation.postal_code,
                    'is_hq': organisation.is_hq,
                    'hq_id': organisation.hq_id,
                    'is_incorporated': organisation.is_incorporated,
                    'date_of_incorporation': organisation.date_of_incorporation,  # noqa
                    'legal_name': organisation.legal_name,
                    'logo': organisation.logo,
                    'logo_id': organisation.logo_id,
                    'banner': organisation.banner,
                    'banner_id': organisation.banner_id,
                    'slogan': organisation.slogan,
                    'phone': organisation.phone,
                    'website': organisation.website,
                    'description': organisation.description,
                    'username': organisation.username,
                    'verified': organisation.verified,
                    'setup_completed': organisation.setup_completed,
                    'can_loan': organisation.can_loan,
                    'created_at': organisation.created_at,
                    'updated_at': organisation.updated_at,
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
        Argument("full_name", location="json",
                 help="The full name of the organisation."),
        Argument("email", location="json",
                 help="The email of the organisation."),
        Argument("date_of_establishment", location="json",
                 help="The date of establishment of the organisation."),
        Argument("country", location="json",
                 help="The country of the organisation."),
        Argument("state", location="json",
                 help="The state of the organisation."),
        Argument("city", location="json",
                 help="The city of the organisation."),
        Argument("address", location="json",
                 help="The address of the organisation."),
        Argument("postal_code", location="json",
                 help="The postal code of the organisation."),
        Argument("is_hq", location="json", type=bool,
                 help="Is this the hq of the organisation."),
        Argument("is_incorporated", location="json", type=bool,
                 help="Is the organisation incorporated."),
        Argument("date_of_incorporation", location="json",
                 help="The date of organisation incorporation."),
        Argument("legal_name", location="json",
                 help="The legal name of the organisation."),
        Argument("logo", location="json",
                 help="The logo of the organisation."),
        Argument("logo_id", location="json",
                 help="The logo id of the organisation."),
        Argument("banner", location="json",
                 help="The banner of the organisation."),
        Argument("banner_id", location="json",
                 help="The banner id of the organisation."),
        Argument("slogan", location="json",
                 help="The slogan the organisation."),
        Argument("phone", location="json",
                 help="The phone of the organisation."),
        Argument("website", location="json",
                 help="The website of the organisation."),
        Argument("description", location="json",
                 help="The description of the organisation."),
        Argument("can_loan", location="json", type=bool,
                 help="Can the organisation give loan."),
    )
    def update_one(id=None, **args):
        """ The function enables the updating of one organisation by id"""

        try:
            organisation = OrganisationModel.query.filter_by(id=id).first()

            if not organisation:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': f"no organisation with id {id} was found",
                }), 404

            if 'full_name' in args and args['full_name'] is not None:
                organisation.full_name = args['full_name']

            if 'email' in args and args['email'] is not None:
                organisation.email = args['email']

            if 'date_of_establishment' in args and args['date_of_establishment'] is not None:  # noqa
                organisation.date_of_establishment = args['date_of_establishment']  # noqa

            if 'country' in args and args['country'] is not None:
                organisation.country = args['country']

            if 'state' in args and args['state'] is not None:
                organisation.state = args['state']

            if 'city' in args and args['city'] is not None:
                organisation.city = args['city']

            if 'address' in args and args['address'] is not None:
                organisation.address = args['address']

            if 'postal_code' in args and args['postal_code'] is not None:
                organisation.postal_code = args['postal_code']

            if 'is_hq' in args and args['is_hq'] is not None:
                organisation.is_hq = args['is_hq']

            if 'is_incorporated' in args and args['is_incorporated'] is not None:  # noqa
                organisation.is_incorporated = args['is_incorporated']

            if 'date_of_incorporation' in args and args['date_of_incorporation'] is not None:  # noqa
                organisation.date_of_incorporation = args['date_of_incorporation']  # noqa

            if 'legal_name' in args and args['legal_name'] is not None:
                organisation.legal_name = args['legal_name']

            if 'logo' in args and args['logo'] is not None:
                organisation.logo = args['logo']

            if 'logo_id' in args and args['logo_id'] is not None:
                organisation.logo_id = args['logo_id']

            if 'banner' in args and args['banner'] is not None:
                organisation.banner = args['banner']

            if 'banner_id' in args and args['banner_id'] is not None:
                organisation.banner_id = args['banner_id']

            if 'slogan' in args and args['slogan'] is not None:
                organisation.slogan = args['slogan']

            if 'phone' in args and args['phone'] is not None:
                organisation.phone = args['phone']

            if 'website' in args and args['website'] is not None:
                organisation.website = args['website']

            if 'description' in args and args['description'] is not None:
                organisation.description = args['description']

            if 'can_loan' in args and args['can_loan'] is not None:
                organisation.can_loan = args['can_loan']

            organisation.save()

            return jsonify({
                'code': 200,
                'code_status': "updated successfully",
                'data': {
                    'id': organisation.id,
                    'full_name': organisation.full_name,
                    'email': organisation.email,
                    'date_of_establishment': organisation.date_of_establishment,  # noqa
                    'country': organisation.country,
                    'state': organisation.state,
                    'city': organisation.city,
                    'address': organisation.address,
                    'postal_code': organisation.postal_code,
                    'is_hq': organisation.is_hq,
                    'hq_id': organisation.hq_id,
                    'is_incorporated': organisation.is_incorporated,
                    'date_of_incorporation': organisation.date_of_incorporation,  # noqa
                    'legal_name': organisation.legal_name,
                    'logo': organisation.logo,
                    'logo_id': organisation.logo_id,
                    'banner': organisation.banner,
                    'banner_id': organisation.banner_id,
                    'slogan': organisation.slogan,
                    'phone': organisation.phone,
                    'website': organisation.website,
                    'description': organisation.description,
                    'username': organisation.username,
                    'verified': organisation.verified,
                    'setup_completed': organisation.setup_completed,
                    'can_loan': organisation.can_loan,
                    'created_at': organisation.created_at,
                    'updated_at': organisation.updated_at,
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
        """ The function enables the deletion of one organisation by id"""

        try:
            organisation = OrganisationModel.query.filter_by(id=id).first()

            if not organisation:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': f"no organisation with id {id} was found",
                }), 404

            organisation.delete()

            # nt_time = NetworkTime.network_time()

            # if organisation.is_deleted is not None and organisation.deleted_at is not None:  # noqa
            #     deletion_date = organisation.deleted_at + timedelta(days=30)

            # if organisation.is_deleted is True:
            #     return jsonify({
            #         'code': 409,
            #         'code_status': "conflict",
            #         'code_message': f"{organisation.full_name} profile is already set for deletion",  # noqa
            #         'data': {
            #             'is_deleted': organisation.is_deleted,
            #             'deleted_at': organisation.deleted_at,
            #             'permanent_deletion': deletion_date
            #         }
            #     }), 409

            # organisation.is_deleted = True
            # organisation.deleted_at = nt_time
            # organisation.save()

            # deletion_date = organisation.deleted_at + timedelta(days=30)

            return jsonify({
                'code': 200,
                'code_status': "deletion successfully",
                'code_message': f"{organisation.full_name} profile will be deleted",  # noqa
                'data': {
                    'is_deleted': organisation.is_deleted,
                    'deleted_at': organisation.deleted_at,
                    # 'permanent_deletion': deletion_date
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
