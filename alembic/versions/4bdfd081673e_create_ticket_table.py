"""create ticket table

Revision ID: 4bdfd081673e
Revises: 
Create Date: 2019-11-11 06:44:33.457644

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4bdfd081673e'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'ticket',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )


def downgrade():
    op.drop_table('ticket')
