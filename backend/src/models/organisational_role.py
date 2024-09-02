"""organisational_role.py

Keyword arguments:
argument -- description
Return: CRUD resources on organisational roles
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


class OrganisationalRoleModel(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ This class defines the organisational role model """

    __tablename__ = "organisational_roles"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4, unique=True)  # noqa
    role = db.Column(db.String(), nullable=False)
    is_top_role = db.Column(db.Boolean(), nullable=False, default=False)
    is_member_role = db.Column(db.Boolean(), nullable=False, default=False)
    role_position = db.Column(db.Integer(), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False, default=nt_time)
    updated_at = db.Column(db.DateTime(), nullable=True, onupdate=nt_time)
    is_deleted = db.Column(db.Boolean(), nullable=False, default=False)
    deleted_at = db.Column(db.DateTime(), nullable=True)

    # foreign keys

    organisation = db.Column(
        UUID(as_uuid=True), db.ForeignKey('organisations.id'), nullable=False)

    # relationships

    members = db.relationship(
        'MemberModel', backref='organisational_roles', lazy=True)
