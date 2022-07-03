"""add content colomn to posts table

Revision ID: 995a01e442d4
Revises: 8b0d03b8d5b3
Create Date: 2022-07-03 13:09:24.493133

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '995a01e442d4'
down_revision = '8b0d03b8d5b3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column("posts", "content")
