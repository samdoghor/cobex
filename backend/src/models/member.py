"""member.py

Keyword arguments:
argument -- description
Return: CRUD resources on members
"""

from uuid import uuid4

from sqlalchemy import UUID
from werkzeug.security import check_password_hash, generate_password_hash

from . import db
from .abc import BaseModel, MetaBaseModel

try:
    from ..utils import NetworkTime
except ImportError:
    from utils import NetworkTime

nt_time = NetworkTime.network_time()


class MemberModel(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ This class defines the member model """

    __tablename__ = "members"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4, unique=True)  # noqa
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    middle_name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, unique=True)
    phone = db.Column(db.String(), nullable=True, unique=True)
    password = db.Column(db.String(), nullable=False)
    date_of_birth = db.Column(db.DateTime(), nullable=False)
    employment_status = db.Column(db.String(), nullable=False)
    occupation = db.Column(db.String(), nullable=False)
    marital_status = db.Column(db.String(), nullable=False)
    country = db.Column(db.String(), nullable=False)
    state = db.Column(db.String(), nullable=False)
    city = db.Column(db.String(), nullable=False)
    address = db.Column(db.String(), nullable=True)
    postal_code = db.Column(db.String(), nullable=False)
    image = db.Column(db.String(), nullable=True)
    image_id = db.Column(db.String(), nullable=True)
    username = db.Column(db.String(), nullable=False, unique=True)
    membership_status = db.Column(db.String(), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False, default=nt_time)
    updated_at = db.Column(db.DateTime(), nullable=True, onupdate=nt_time)
    is_deleted = db.Column(db.Boolean(), nullable=False, default=False)
    deleted_at = db.Column(db.DateTime(), nullable=True)

    # foreign keys

    organisational_role = db.Column(
        UUID(as_uuid=True), db.ForeignKey('organisational_roles.id'),
        nullable=False)

    organisation = db.Column(
        UUID(as_uuid=True), db.ForeignKey('organisations.id'), nullable=False)

    # relationships

    member_socials = db.relationship(
        'MemberSocialModel', backref='members', lazy=True,
        cascade='all, delete-orphan')

    levy_payments = db.relationship(
        'LevyPaymentModel', backref='members', lazy=True)

    loans = db.relationship(
        'LoanModel', backref='members', lazy=True)

    loan_approvals = db.relationship(
        'LoanApprovalModel', backref='members', lazy=True)

    loan_payments = db.relationship(
        'LoanPaymentModel', backref='loans', lazy=True)

    # utilities

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
