"""organisation_social.py

Keyword arguments:
argument -- description
Return: CRUD resources on organisation socials
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


class OrganisationSocialModel(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ This class defines the organisation social model """

    __tablename__ = "organisation_socials"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4, unique=True)  # noqa
    name = db.Column(db.String(), nullable=False)
    link = db.Column(db.String(), nullable=False, unique=True)
    created_at = db.Column(db.DateTime(), nullable=False, default=nt_time)
    updated_at = db.Column(db.DateTime(), nullable=True, onupdate=nt_time)
    is_deleted = db.Column(db.Boolean(), nullable=False, default=False)
    deleted_at = db.Column(db.DateTime(), nullable=True)

    # foreign keys

    organisation = db.Column(
        UUID(as_uuid=True), db.ForeignKey('organisations.id'), nullable=False)
