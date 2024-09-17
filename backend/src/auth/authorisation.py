"""authorisation.py

Keyword arguments:
argument -- description
Return: return_description
"""

from datetime import timedelta

import jwt
from flask import jsonify
from sqlalchemy.exc import (DataError, InterfaceError, OperationalError,
                            PendingRollbackError, ProgrammingError)
from werkzeug.exceptions import BadRequest, MethodNotAllowed, NotFound

try:
    from ..utils import NetworkTime
    from .. import config
except ImportError:
    from utils import NetworkTime
    import config

nt_time = NetworkTime.network_time()


class Authorisation:
    """ The class is concern with the authorisation API  """

    @staticmethod
    def auth_encoder(id, first_name, last_name):
        """ The function enables generating token """

        try:
            payload = {
                'exp': nt_time + timedelta(
                    days=0, seconds=int(config.token_expiration)),
                'iat': nt_time,
                'sub': str(id),
                'name': f'{first_name} {last_name}'
            }

            return jwt.encode(
                payload,
                config.application_secret_key,
                algorithm=config.encryption_algorithm
            )

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
    def auth_decoder(acess_token):
        """ The function enables decoding token"""

        try:
            payload = jwt.decode(acess_token, config.application_secret_key,
                                 algorithms=[config.encryption_algorithm])
            return payload
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

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
