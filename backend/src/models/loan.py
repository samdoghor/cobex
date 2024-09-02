"""loan.py

Keyword arguments:
argument -- description
Return: CRUD resources on loans
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


class LoanModel(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ This class defines the loan model """

    __tablename__ = "loans"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4, unique=True)  # noqa
    amount = db.Column(db.String(), nullable=False)
    due_date = db.Column(db.DateTime(), nullable=False)
    interest_at = db.Column(db.Text, nullable=False)
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

    # relationships

    loan_approvals = db.relationship(
        'LoanApprovalModel', backref='loans', lazy=True,
        cascade='all, delete-orphan')

    loan_payments = db.relationship(
        'LoanPaymentModel', backref='loans', lazy=True,
        cascade='all, delete-orphan')
