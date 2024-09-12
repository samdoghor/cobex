"""event.py

Keyword arguments:
argument -- description
Return: CRUD resources on events
"""

from uuid import uuid4

from sqlalchemy import UUID

from . import db
from .abc import BaseModel, MetaBaseModel

try:
    from ..utils import NetworkTime
except ImportError:
    from utils import NetworkTime

nt_time = NetworkTime.network_time()


class EventModel(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ This class defines the event model """

    __tablename__ = "events"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4, unique=True)  # noqa
    title = db.Column(db.String(), nullable=False)
    date = db.Column(db.DateTime(), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(), nullable=True)
    image_id = db.Column(db.String(), nullable=True)
    created_at = db.Column(db.DateTime(), nullable=False, default=nt_time)
    updated_at = db.Column(db.DateTime(), nullable=True, onupdate=nt_time)
    is_deleted = db.Column(db.Boolean(), nullable=False, default=False)
    deleted_at = db.Column(db.DateTime(), nullable=True)

    # foreign keys

    organisation = db.Column(
        UUID(as_uuid=True), db.ForeignKey('organisations.id'), nullable=False)
    member = db.Column(
        UUID(as_uuid=True), db.ForeignKey('members.id'), nullable=False)
