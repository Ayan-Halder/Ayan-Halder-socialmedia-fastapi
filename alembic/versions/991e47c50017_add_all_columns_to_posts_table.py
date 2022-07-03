"""add all columns to posts table

Revision ID: 991e47c50017
Revises: 773ad3bdb26d
Create Date: 2022-07-03 13:41:18.513978

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '991e47c50017'
down_revision = '773ad3bdb26d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"))
    op.add_column("posts", sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False))


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
