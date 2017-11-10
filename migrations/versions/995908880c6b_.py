"""empty message

Revision ID: 995908880c6b
Revises: 735f912dcb55
Create Date: 2017-10-30 21:54:54.661280

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '995908880c6b'
down_revision = '735f912dcb55'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('results',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tag', sa.String(length=20), nullable=True),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('ref', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('snp500',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('sp500', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('date')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('snp500')
    op.drop_table('results')
    # ### end Alembic commands ###