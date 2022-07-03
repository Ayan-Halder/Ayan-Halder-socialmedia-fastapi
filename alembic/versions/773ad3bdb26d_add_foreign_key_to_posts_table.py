"""add foreign key to posts table

Revision ID: 773ad3bdb26d
Revises: af3b94dbc2a5
Create Date: 2022-07-03 13:35:38.709649

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '773ad3bdb26d'
down_revision = 'af3b94dbc2a5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("post_users_fk", source_table="posts", referent_table="users", local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE")



def downgrade() -> None:
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
