"""new fields in user model

Revision ID: d24a15323f90
Revises: bf1002d1f8e3
Create Date: 2020-06-24 15:36:46.311951

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd24a15323f90'
down_revision = 'bf1002d1f8e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('dob', sa.String(length=64), nullable=True))
    op.add_column('user', sa.Column('firstname', sa.String(length=64), nullable=True))
    op.add_column('user', sa.Column('lastname', sa.String(length=64), nullable=True))
    op.add_column('user', sa.Column('middlename', sa.String(length=64), nullable=True))
    op.add_column('user', sa.Column('mobile', sa.String(length=64), nullable=True))
    op.add_column('user', sa.Column('pob', sa.String(length=64), nullable=True))
    op.add_column('user', sa.Column('tob', sa.String(length=64), nullable=True))
    op.create_index(op.f('ix_user_dob'), 'user', ['dob'], unique=True)
    op.create_index(op.f('ix_user_firstname'), 'user', ['firstname'], unique=True)
    op.create_index(op.f('ix_user_lastname'), 'user', ['lastname'], unique=True)
    op.create_index(op.f('ix_user_middlename'), 'user', ['middlename'], unique=True)
    op.create_index(op.f('ix_user_mobile'), 'user', ['mobile'], unique=True)
    op.create_index(op.f('ix_user_pob'), 'user', ['pob'], unique=True)
    op.create_index(op.f('ix_user_tob'), 'user', ['tob'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_tob'), table_name='user')
    op.drop_index(op.f('ix_user_pob'), table_name='user')
    op.drop_index(op.f('ix_user_mobile'), table_name='user')
    op.drop_index(op.f('ix_user_middlename'), table_name='user')
    op.drop_index(op.f('ix_user_lastname'), table_name='user')
    op.drop_index(op.f('ix_user_firstname'), table_name='user')
    op.drop_index(op.f('ix_user_dob'), table_name='user')
    op.drop_column('user', 'tob')
    op.drop_column('user', 'pob')
    op.drop_column('user', 'mobile')
    op.drop_column('user', 'middlename')
    op.drop_column('user', 'lastname')
    op.drop_column('user', 'firstname')
    op.drop_column('user', 'dob')
    # ### end Alembic commands ###
