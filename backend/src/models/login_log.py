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


class LoginLogModel(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ This class defines the event model """

    __tablename__ = "login_logs"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4, unique=True)  # noqa
    user_id = db.Column(db.String(), nullable=False)
    timestamp = db.Column(db.DateTime(), nullable=False)
    status = db.Column(db.String(), nullable=False)
    ip_address = db.Column(db.String(), nullable=True)
    full_name = db.Column(db.String(), nullable=True)
    created_at = db.Column(db.DateTime(), nullable=False, default=nt_time)
    updated_at = db.Column(db.DateTime(), nullable=True, onupdate=nt_time)
    is_deleted = db.Column(db.Boolean(), nullable=False, default=False)
    deleted_at = db.Column(db.DateTime(), nullable=True)
