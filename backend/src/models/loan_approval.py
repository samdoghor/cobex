"""loan_approval.py

Keyword arguments:
argument -- description
Return: CRUD resources on loan approvals
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


class LoanApprovalModel(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ This class defines the loan approval model """

    __tablename__ = "loan_approvals"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4, unique=True)  # noqa
    created_at = db.Column(db.DateTime(), nullable=False, default=nt_time)
    updated_at = db.Column(db.DateTime(), nullable=True, onupdate=nt_time)
    is_deleted = db.Column(db.Boolean(), nullable=False, default=False)
    deleted_at = db.Column(db.DateTime(), nullable=True)

    # foreign keys

    organisation = db.Column(
        UUID(as_uuid=True), db.ForeignKey('organisations.id'), nullable=False)

    member = db.Column(
        UUID(as_uuid=True), db.ForeignKey('members.id'), nullable=False)

    loan = db.Column(
        UUID(as_uuid=True), db.ForeignKey('loans.id'), nullable=False)
