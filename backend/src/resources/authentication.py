"""authentication.py

Keyword arguments:
argument -- description
Return: return_description
"""

from flask import current_app, jsonify, session
from flask_restful import Resource
from flask_restful.reqparse import Argument
from sqlalchemy.exc import (DataError, InterfaceError, OperationalError,
                            PendingRollbackError, ProgrammingError)
from werkzeug.exceptions import BadRequest, MethodNotAllowed, NotFound

try:
    from ..models import MemberModel
    from ..utils.parse_params import parse_params
    from ..auth import Authorisation
except ImportError:
    from models import MemberModel
    from utils.parse_params import parse_params
    from auth import Authorisation


class AuthenticationResource(Resource):
    """ The class is concern with the authentication API  """

    @staticmethod
    @parse_params(
        Argument("email", location="json", required=True,
                 help="The email of the user."),
        Argument("password", location="json", required=True,
                 help="The password of the user."),
    )
    def login(email, password):
        """ The function enables the user's login functionality"""

        try:
            member = MemberModel.query.filter_by(email=email).first()

            if not email:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': "email is missing"
                }), 404

            if not password:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': "password is missing"
                }), 404

            if "@"not in email:
                return jsonify({
                    'code': 404,
                    'code_status': "data error",
                    'code_message': "email is invalid"
                }), 404

            if not member:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': f"{email} doesn't have an account"
                }), 404

            password = member.check_password(password)

            if not password:
                return jsonify({
                    'code': 401,
                    'code_status': "unauthorised",
                    'code_message': "incorrect password"
                }), 401

            if member:
                if password:

                    current_app.session_interface.regenerate(session)
                    session['id'] = member.id
                    session['email'] = member.email

                    access_token = Authorisation.auth_encoder(
                        member.id, member.first_name, member.last_name)
                    session['access_token'] = access_token

                    return jsonify({
                        'code': 200,
                        'code_status': "logged in successfully",
                        'data': {
                            'id': member.id,
                            'email': member.email,
                            'access_token': access_token
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
    def logout():
        """ The function enables the creation of an event"""

        try:
            session.clear()
            session.modified = True

            return jsonify({
                'code': 200,
                'code_status': "logged out successfully",
                'code_message': "You have been logged out successfully"
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
