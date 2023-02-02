"""empty message

Revision ID: 1186e8060234
Revises: 0eb1159064b1
Create Date: 2023-02-02 14:58:49.553816

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1186e8060234'
down_revision = '0eb1159064b1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('salt', sa.String(length=64), nullable=False))
        batch_op.add_column(sa.Column('created_at', sa.TIMESTAMP(), nullable=False))
        batch_op.add_column(sa.Column('updated_at', sa.TIMESTAMP(), nullable=False))
        batch_op.add_column(sa.Column('deleted_at', sa.TIMESTAMP(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('deleted_at')
        batch_op.drop_column('updated_at')
        batch_op.drop_column('created_at')
        batch_op.drop_column('salt')

    # ### end Alembic commands ###
