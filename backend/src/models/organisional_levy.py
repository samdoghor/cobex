"""organisational_levy.py

Keyword arguments:
argument -- description
Return: CRUD resources on organisational levies
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


class OrganisationalLevyModel(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ This class defines the organisational levy model """

    __tablename__ = "organisational_levies"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4, unique=True)  # noqa
    levy_name = db.Column(db.String(), nullable=False)
    interval = db.Column(db.String(), nullable=False)
    amount = db.Column(db.Integer(), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False, default=nt_time)
    updated_at = db.Column(db.DateTime(), nullable=True, onupdate=nt_time)
    is_deleted = db.Column(db.Boolean(), nullable=False, default=False)
    deleted_at = db.Column(db.DateTime(), nullable=True)

    # foreign keys

    organisation = db.Column(
        UUID(as_uuid=True), db.ForeignKey('organisations.id'), nullable=False)

    # relationships

    levy_payments = db.relationship(
        'LevyPaymentModel', backref='organisational_levies', lazy=True,
        cascade='all, delete-orphan')
