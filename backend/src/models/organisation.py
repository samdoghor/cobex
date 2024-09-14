"""organisation.py

Keyword arguments:
argument -- description
Return: CRUD resources on organisations
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


class OrganisationModel(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ This class defines the organisation model """

    __tablename__ = "organisations"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4, unique=True)  # noqa
    full_name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, unique=True)
    date_of_establishment = db.Column(db.DateTime(), nullable=True)
    country = db.Column(db.String(), nullable=True)
    state = db.Column(db.String(), nullable=True)
    city = db.Column(db.String(), nullable=True)
    address = db.Column(db.String(), nullable=True)
    postal_code = db.Column(db.String(), nullable=True)
    is_hq = db.Column(db.Boolean(), nullable=False, default=False)
    hq_id = db.Column(UUID(as_uuid=True), default=uuid4, nullable=True)
    is_incorporated = db.Column(db.Boolean(), nullable=False, default=False)
    date_of_incorporation = db.Column(db.DateTime(), nullable=True)
    legal_name = db.Column(db.String(), nullable=True)
    logo = db.Column(db.String(), nullable=True)
    logo_id = db.Column(db.String(), nullable=True)
    banner = db.Column(db.String(), nullable=True)
    banner_id = db.Column(db.String(), nullable=True)
    slogan = db.Column(db.String(), nullable=True)
    phone = db.Column(db.String(), nullable=True)
    website = db.Column(db.String(), nullable=True)
    description = db.Column(db.Text, nullable=True)
    username = db.Column(db.String(), nullable=False, unique=True)
    verified = db.Column(db.Boolean(), nullable=False, default=False)
    setup_completed = db.Column(db.Boolean(), nullable=False, default=False)
    can_loan = db.Column(db.Boolean(), nullable=False, default=False)
    created_at = db.Column(db.DateTime(), nullable=False, default=nt_time)
    updated_at = db.Column(db.DateTime(), nullable=True, onupdate=nt_time)
    is_deleted = db.Column(db.Boolean(), nullable=False, default=False)
    deleted_at = db.Column(db.DateTime(), nullable=True)

    # relationships

    organisation_socials = db.relationship(
        'OrganisationSocialModel', backref='organisations', lazy=True,
        cascade='all, delete-orphan')

    organisation_roles = db.relationship(
        'OrganisationalRoleModel', backref='organisations', lazy=True,
        cascade='all, delete-orphan')

    members = db.relationship(
        'MemberModel', backref='organisations', lazy=True,
        cascade='all, delete-orphan')

    organisation_accounts = db.relationship(
        'OrganisationAccountModel', backref='organisations', lazy=True,
        cascade='all, delete-orphan')

    organisational_levies = db.relationship(
        'OrganisationalLevyModel', backref='organisations', lazy=True,
        cascade='all, delete-orphan')

    levy_payments = db.relationship(
        'LevyPaymentModel', backref='organisations', lazy=True,
        cascade='all, delete-orphan')

    events = db.relationship(
        'EventModel', backref='organisations', lazy=True,
        cascade='all, delete-orphan')

    loans = db.relationship(
        'LoanModel', backref='organisations', lazy=True,
        cascade='all, delete-orphan')

    loan_approvals = db.relationship(
        'LoanApprovalModel', backref='organisations', lazy=True,
        cascade='all, delete-orphan')

    loan_payments = db.relationship(
        'LoanPaymentModel', backref='organisations', lazy=True,
        cascade='all, delete-orphan')
