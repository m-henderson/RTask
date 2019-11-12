"""add userid column

Revision ID: 9dbc7d2409e8
Revises: 4bdfd081673e
Create Date: 2019-11-12 05:01:39.717320

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9dbc7d2409e8'
down_revision = '4bdfd081673e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('ticket', sa.Column('userId', sa.String(50), nullable=False))


def downgrade():
    op.drop_column('ticket', 'userId')
