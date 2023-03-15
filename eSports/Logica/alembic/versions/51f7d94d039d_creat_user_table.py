"""creat user table

Revision ID: 51f7d94d039d
Revises: 
Create Date: 2023-03-07 17:46:35.455215

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51f7d94d039d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('nick_name', sa.String(50), nullable=False),
        sa.Column('fullname', sa.Unicode(200))
    )


def downgrade() -> None:
    op.drop_table('users')
