"""update models users

Revision ID: 4e346057b63d
Revises: db1f4f087800
Create Date: 2022-06-07 23:04:02.266790

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e346057b63d'
down_revision = 'db1f4f087800'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('username', sa.Unicode(), nullable=True))
    op.drop_column('users', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('name', sa.VARCHAR(), nullable=True))
    op.drop_column('users', 'username')
    # ### end Alembic commands ###