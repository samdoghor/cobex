"""member.py

Keyword arguments:
argument -- description
Return: return_description
"""
import secrets
from datetime import timedelta
from flask import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument
from sqlalchemy.exc import (DataError, IntegrityError, InterfaceError,
                            OperationalError, PendingRollbackError,
                            ProgrammingError)
from werkzeug.exceptions import BadRequest, MethodNotAllowed, NotFound

try:
    from ..models import MemberModel, OrganisationModel
    from ..utils.parse_params import parse_params
    from ..utils import NetworkTime
except ImportError:
    from models import MemberModel, OrganisationModel
    from utils.parse_params import parse_params
    from utils import NetworkTime


class MemberResource(Resource):
    """ The class is concern with the member's CRUD API  """

    @staticmethod
    @parse_params(
        Argument("first_name", location="json", required=True,
                 help="The first name of the member."),
        Argument("last_name", location="json", required=True,
                 help="The last name of the member."),
        Argument("email", location="json", required=True,
                 help="The email of the member."),
        Argument("password", location="json", required=True,
                 help="The password of the member."),
        Argument("organisation", location="json", required=True,
                 help="The organisation the member belong to."),
        Argument("organisational_role", location="json", required=True,
                 help="The organisation role of the member"),
    )
    def create(first_name, last_name, email, password, organisation,
               organisational_role):
        """ The function enables the creation of an member"""

        try:
            member_email = MemberModel.query.filter_by(
                email=email).first()

            members = MemberModel.query.all()

            organisation_email = OrganisationModel.query.filter_by(
                email=email).first()

            if member_email is not None:
                return jsonify({
                    'code': 409,
                    'code_status': "conflict",
                    'code_message': f"{email} already has an account",
                }), 409

            if organisation_email is not None:
                return jsonify({
                    'code': 409,
                    'code_status': "conflict",
                    'code_message': f"{email} was used for an organisation account"  # noqa
                }), 409

            username = secrets.token_urlsafe(8)

            for member in members:
                while member.username == username:
                    username = secrets.token_urlsafe(8)

            new_member = MemberModel(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                organisation=organisation,
                organisational_role=organisational_role,
            )
            new_member.set_password(password)
            new_member.save()

            return jsonify({
                'code': 201,
                'code_status': "created successfully",
                'data': {
                    'id': new_member.id,
                    'first_name': new_member.first_name,
                    'last_name': new_member.last_name,
                    'email': new_member.email,
                    'username': new_member.username,
                    'membership_status': new_member.membership_status,
                    'verified': new_member.verified,
                    'setup_completed': new_member.setup_completed,
                    'organisation': new_member.organisation,
                    'organisational_role': new_member.organisational_role,
                    'created_at': new_member.created_at,
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
        """ The function enables the reading of all members"""

        try:
            members = MemberModel.query.all()

            if not members:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': "no member found",
                }), 404

            members_list = []

            for member in members:
                members_list.append({
                    'id': member.id,
                    'first_name': member.first_name,
                    'last_name': member.last_name,
                    'middle_name': member.middle_name,
                    'email': member.email,
                    'phone': member.phone,
                    'date_of_birth': member.date_of_birth,
                    'employment_status': member.employment_status,
                    'occupation': member.occupation,
                    'marital_status': member.marital_status,
                    'country': member.country,
                    'state': member.state,
                    'city': member.city,
                    'address': member.address,
                    'postal_code': member.postal_code,
                    'image': member.image,
                    'image_id': member.image_id,
                    'username': member.username,
                    'membership_status': member.membership_status,
                    'verified': member.verified,
                    'setup_completed': member.setup_completed,
                    'organisation': member.organisation,
                    'organisational_role': member.organisational_role,
                    'created_at': member.created_at,
                    'updated_at': member.updated_at,
                })

            return jsonify({
                'code': 200,
                'code_status': "retrieved successfully",
                'data': members_list,
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
        """ The function enables the reading of one member by id"""

        try:
            member = MemberModel.query.filter_by(id=id).first()

            if not member:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': f"no member with id {id} was found",
                }), 404

            return jsonify({
                'code': 200,
                'code_status': "retrieved successfully",
                'data': {
                    'id': member.id,
                    'first_name': member.first_name,
                    'last_name': member.last_name,
                    'middle_name': member.middle_name,
                    'email': member.email,
                    'phone': member.phone,
                    'date_of_birth': member.date_of_birth,
                    'employment_status': member.employment_status,
                    'occupation': member.occupation,
                    'marital_status': member.marital_status,
                    'country': member.country,
                    'state': member.state,
                    'city': member.city,
                    'address': member.address,
                    'postal_code': member.postal_code,
                    'image': member.image,
                    'image_id': member.image_id,
                    'username': member.username,
                    'membership_status': member.membership_status,
                    'verified': member.verified,
                    'setup_completed': member.setup_completed,
                    'organisation': member.organisation,
                    'organisational_role': member.organisational_role,
                    'created_at': member.created_at,
                    'updated_at': member.updated_at,
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
        Argument("first_name", location="json",
                 help="The first name of the member."),
        Argument("last_name", location="json",
                 help="The last name of the member."),
        Argument("middle_name", location="json",
                 help="The middle name of the member."),
        Argument("email", location="json",
                 help="The email of the member."),
        Argument("phone", location="json",
                 help="The phone of the member."),
        Argument("date_of_birth", location="json",
                 help="The date of birth of the member."),
        Argument("employment_status", location="json",
                 help="The employment status of the member."),
        Argument("occupation", location="json",
                 help="The occupation of the member."),
        Argument("marital_status", location="json",
                 help="The marital status of the member."),
        Argument("country", location="json",
                 help="The country od the member."),
        Argument("state", location="json",
                 help="The date of member incorporation."),
        Argument("city", location="json",
                 help="The city of the member."),
        Argument("address", location="json",
                 help="The address of the member."),
        Argument("state", location="json",
                 help="The state of the member."),
        Argument("postal_code", location="json",
                 help="The postal code of the member."),
        Argument("image", location="json",
                 help="The image of the member."),
        Argument("image_id", location="json",
                 help="The image id of the member."),
        Argument("username", location="json",
                 help="The username the member."),
        Argument("membership_status", location="json",
                 help="The membership_status of the member."),
        Argument("verified", location="json",
                 help="Is the member verified."),
        Argument("setup_completed", location="json",
                 help="Is the setup of the member complete."),
        Argument("organisational_role", location="json",
                 help="The organisational_role of the member."),
    )
    def update_one(id=None, **args):
        """ The function enables the updating of one member by id"""

        try:
            member = MemberModel.query.filter_by(id=id).first()

            if not member:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': f"no member with id {id} was found",
                }), 404

            if 'first_name' in args and args['first_name'] is not None:
                member.first_name = args['first_name']

            if 'last_name' in args and args['last_name'] is not None:
                member.last_name = args['last_name']

            if 'middle_name' in args and args['middle_name'] is not None:
                member.middle_name = args['middle_name']

            if 'email' in args and args['email'] is not None:
                member.email = args['email']

            if 'membership_status' in args and args['membership_status'] is not None:  # noqa
                member.membership_status = args['membership_status']

            if 'date_of_birth' in args and args['date_of_birth'] is not None:
                member.date_of_birth = args['date_of_birth']

            if 'employment_status' in args and args['employment_status'] is not None:  # noqa
                member.employment_status = args['employment_status']

            if 'occupation' in args and args['occupation'] is not None:
                member.occupation = args['occupation']

            if 'marital_status' in args and args['marital_status'] is not None:
                member.marital_status = args['marital_status']

            if 'country' in args and args['country'] is not None:
                member.country = args['country']

            if 'state' in args and args['state'] is not None:
                member.state = args['state']

            if 'city' in args and args['city'] is not None:
                member.city = args['city']

            if 'address' in args and args['address'] is not None:
                member.address = args['address']

            if 'postal_code' in args and args['postal_code'] is not None:
                member.postal_code = args['postal_code']

            if 'image' in args and args['image'] is not None:
                member.image = args['image']

            if 'image_id' in args and args['image_id'] is not None:
                member.image_id = args['image_id']

            if 'username' in args and args['username'] is not None:
                member.username = args['username']

            if 'phone' in args and args['phone'] is not None:
                member.phone = args['phone']

            if 'verified' in args and args['verified'] is not None:
                member.verified = args['verified']

            if 'setup_completed' in args and args['setup_completed'] is not None:  # noqa
                member.setup_completed = args['setup_completed']

            if 'organisational_role' in args and args['organisational_role'] is not None:  # noqa
                member.organisational_role = args['organisational_role']

            member.save()

            return jsonify({
                'code': 200,
                'code_status': "updated successfully",
                'data': {
                    'id': member.id,
                    'first_name': member.first_name,
                    'last_name': member.last_name,
                    'middle_name': member.middle_name,
                    'email': member.email,
                    'phone': member.phone,
                    'date_of_birth': member.date_of_birth,
                    'employment_status': member.employment_status,
                    'occupation': member.occupation,
                    'marital_status': member.marital_status,
                    'country': member.country,
                    'state': member.state,
                    'city': member.city,
                    'address': member.address,
                    'postal_code': member.postal_code,
                    'image': member.image,
                    'image_id': member.image_id,
                    'username': member.username,
                    'membership_status': member.membership_status,
                    'verified': member.verified,
                    'setup_completed': member.setup_completed,
                    'organisation': member.organisation,
                    'organisational_role': member.organisational_role,
                    'created_at': member.created_at,
                    'updated_at': member.updated_at,
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
        """ The function enables the deletion of one member by id"""

        try:
            member = MemberModel.query.filter_by(id=id).first()

            if not member:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': f"no member with id {id} was found",
                }), 404

            nt_time = NetworkTime.network_time()

            if member.deleted_at is not None:
                deletion_date = member.deleted_at + timedelta(days=30)

            if member.is_deleted is True:
                return jsonify({
                    'code': 409,
                    'code_status': "conflict",
                    'code_message': f"{member.first_name} {member.last_name} profile is already set for deletion",  # noqa
                    'data': {
                        'is_deleted': member.is_deleted,
                        'deleted_at': member.deleted_at,
                        'permanent_deletion': deletion_date
                    }
                }), 409

            member.is_deleted = True
            member.deleted_at = nt_time
            member.save()

            deletion_date = member.deleted_at + timedelta(days=30)

            return jsonify({
                'code': 200,
                'code_status': "deleted successfully",
                'code_message': f"{member.first_name} {member.last_name} profile will be deleted",  # noqa
                'data': {
                    'is_deleted': member.is_deleted,
                    'deleted_at': member.deleted_at,
                    'permanent_deletion': deletion_date
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
