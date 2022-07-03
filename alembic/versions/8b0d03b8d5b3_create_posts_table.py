"""create posts table

Revision ID: 8b0d03b8d5b3
Revises: 
Create Date: 2022-07-03 12:57:48.228047

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b0d03b8d5b3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("posts", sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
    sa.Column("title", sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_table("posts")
