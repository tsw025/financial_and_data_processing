"""fix update trader model missing timestamps

Revision ID: 606b354140e8
Revises: 4e7efbe4b093
Create Date: 2023-08-01 21:20:15.477164

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '606b354140e8'
down_revision = '4e7efbe4b093'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('trader', sa.Column('created_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"), nullable=True))
    op.add_column('trader', sa.Column('updated_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('trader', 'updated_at')
    op.drop_column('trader', 'created_at')
    # ### end Alembic commands ###