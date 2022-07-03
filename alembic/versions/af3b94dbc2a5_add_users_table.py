"""add users table

Revision ID: af3b94dbc2a5
Revises: 995a01e442d4
Create Date: 2022-07-03 13:14:48.667726

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af3b94dbc2a5'
down_revision = '995a01e442d4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"))


def downgrade() -> None:
    op.drop_table("users")
