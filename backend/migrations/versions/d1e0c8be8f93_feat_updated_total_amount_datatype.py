"""feat: updated total amount datatype

Revision ID: d1e0c8be8f93
Revises: 327f6d3b805a
Create Date: 2024-09-12 16:59:39.193019

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1e0c8be8f93'
down_revision = '327f6d3b805a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('loans', schema=None) as batch_op:
        batch_op.alter_column('total_amount',
               existing_type=sa.INTEGER(),
               type_=sa.Float(),
               existing_nullable=False,
               existing_server_default=sa.text('5'))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('loans', schema=None) as batch_op:
        batch_op.alter_column('total_amount',
               existing_type=sa.Float(),
               type_=sa.INTEGER(),
               existing_nullable=False,
               existing_server_default=sa.text('5'))

    # ### end Alembic commands ###
