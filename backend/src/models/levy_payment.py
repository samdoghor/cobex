"""levy_payment.py

Keyword arguments:
argument -- description
Return: CRUD resources on levy payment
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


class LevyPaymentModel(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ This class defines the levy payment model """

    __tablename__ = "levy_payments"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4, unique=True)  # noqa
    amount = db.Column(db.Integer(), nullable=False)
    reference = db.Column(db.String(), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False, default=nt_time)
    updated_at = db.Column(db.DateTime(), nullable=True, onupdate=nt_time)
    is_deleted = db.Column(db.Boolean(), nullable=False, default=False)
    deleted_at = db.Column(db.DateTime(), nullable=True)

    # foreign keys

    levy = db.Column(
        UUID(as_uuid=True), db.ForeignKey(
            'organisational_levies.id'), nullable=False)

    member = db.Column(
        UUID(as_uuid=True), db.ForeignKey('members.id'), nullable=False)

    organisation = db.Column(
        UUID(as_uuid=True), db.ForeignKey('organisations.id'), nullable=False)
