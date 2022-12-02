"""empty message

Revision ID: 12dff781590e
Revises: 
Create Date: 2022-12-01 22:44:19.377886

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12dff781590e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('age', sa.String(length=30), nullable=True),
    sa.Column('address', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
