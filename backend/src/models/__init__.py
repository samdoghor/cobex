from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .event import EventModel
from .levy_payment import LevyPaymentModel
from .loan_approval import LoanApprovalModel
from .loan_payment import LoanPaymentModel
from .loan import LoanModel
from .member_social import MemberSocialModel
from .member import MemberModel
from .organisation_account import OrganisationAccountModel
from .organisation_social import OrganisationSocialModel
from .organisation import OrganisationModel
from .organisational_role import OrganisationalRoleModel
from .organisional_levy import OrganisationalLevyModel
