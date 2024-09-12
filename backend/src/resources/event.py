"""event.py

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
    from ..models.event import EventModel
    from ..utils.parse_params import parse_params
except ImportError:
    from models import EventModel
    from utils.parse_params import parse_params


class EventResource(Resource):
    """ The class is concern with the event's CRUD API  """

    @staticmethod
    @parse_params(
        Argument("title", location="json", required=True,
                 help="The title of the event."),
        Argument("date", location="json", required=True,
                 help="The date of the event."),
        Argument("description", location="json", required=True,
                 help="The description of the event."),
        Argument("image", location="json",
                 help="The image of the event."),
        Argument("image_id", location="json",
                 help="The image id of the event."),
        Argument("organisation", location="json",
                 help="The organisation id of the event."),
        Argument("member", location="json",
                 help="The member id of the event."),
    )
    def create(title, date, description, image, image_id, organisation,
               member):
        """ The function enables the creation of an event"""

        try:
            new_event = EventModel(
                title=title,
                date=date,
                description=description,
                image=image,
                image_id=image_id,
                organisation=organisation,
                member=member,
            )
            new_event.save()

            return jsonify({
                'code': 201,
                'code_status': "created successfully",
                'data': {
                    'id': new_event.id,
                    'title': new_event.title,
                    'date': new_event.date,
                    'description': new_event.description,
                    'image': new_event.image,
                    'image_id': new_event.image_id,
                    'organisation': new_event.organisation,
                    'member': new_event.member,
                    'created_at': new_event.created_at,
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
        """ The function enables the reading of all events"""

        try:
            events = EventModel.query.all()

            if not events:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': "no event found",
                }), 404

            events_list = []

            for event in events:
                events_list.append({
                    'id': event.id,
                    'title': event.title,
                    'date': event.date,
                    'description': event.description,
                    'image': event.image,
                    'image_id': event.image_id,
                    'organisation': event.organisation,
                    'member': event.member,
                    'created_at': event.created_at,
                    'updated_at': event.updated_at,
                })

            return jsonify({
                'code': 200,
                'code_status': "retrieved successfully",
                'data': events_list,
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
        """ The function enables the reading of one event by id"""

        try:
            event = EventModel.query.filter_by(id=id).first()

            if not event:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': f"no event with id {id} was found",
                }), 404

            return jsonify({
                'code': 200,
                'code_status': "retrieved successfully",
                'data': {
                    'id': event.id,
                    'title': event.title,
                    'date': event.date,
                    'description': event.description,
                    'image': event.image,
                    'image_id': event.image_id,
                    'organisation': event.organisation,
                    'member': event.member,
                    'created_at': event.created_at,
                    'updated_at': event.updated_at,
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
        Argument("title", location="json",
                 help="The title of the event."),
        Argument("date", location="json",
                 help="The date of the event."),
        Argument("description", location="json",
                 help="The description of the event."),
        Argument("image", location="json",
                 help="The image of the event."),
        Argument("image_id", location="json",
                 help="The image id of the event."),
    )
    def update_one(id=None, **args):
        """ The function enables the updating of one event by id"""

        try:
            event = EventModel.query.filter_by(id=id).first()

            if not event:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': f"no event with id {id} was found",
                }), 404

            if 'title' in args and args['title'] is not None:
                event.title = args['title']

            if 'date' in args and args['date'] is not None:
                event.date = args['date']

            if 'description' in args and args['description'] is not None:
                event.description = args['description']

            if 'image' in args and args['image'] is not None:
                event.image = args['image']

            if 'image_id' in args and args['image_id'] is not None:
                event.image_id = args['image_id']

            event.save()

            return jsonify({
                'code': 200,
                'code_status': "updated successfully",
                'data': {
                    'id': event.id,
                    'title': event.title,
                    'date': event.date,
                    'description': event.description,
                    'image': event.image,
                    'image_id': event.image_id,
                    'organisation': event.organisation,
                    'member': event.member,
                    'created_at': event.created_at,
                    'updated_at': event.updated_at,
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
        """ The function enables the deletion of one event by id"""

        try:
            event = EventModel.query.filter_by(id=id).first()

            if not event:
                return jsonify({
                    'code': 404,
                    'code_status': "not found",
                    'code_message': f"no event with id {id} was found",
                }), 404

            event.delete()

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
