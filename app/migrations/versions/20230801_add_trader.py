"""add Trader

Revision ID: 4e7efbe4b093
Revises: 
Create Date: 2023-08-01 19:19:58.753936

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e7efbe4b093'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('trader',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('transaction_type', sa.String(), nullable=False),
    sa.Column('assetType', sa.String(length=50), nullable=False),
    sa.Column('assetValue', sa.Float(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_trader'))
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('trader')
    # ### end Alembic commands ###
