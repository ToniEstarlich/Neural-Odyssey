"""empty message

Revision ID: 2c93f515cd85
Revises: 
Create Date: 2025-02-08 15:36:01.211741

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c93f515cd85'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Drop foreign key constraints first
    op.drop_constraint('progress_course_id_fkey', 'progress', type_='foreignkey')
    op.drop_constraint('progress_user_id_fkey', 'progress', type_='foreignkey')
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('course')
    op.drop_table('progress')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('user_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('usename', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='user_pkey'),
    sa.UniqueConstraint('email', name='user_email_key'),
    sa.UniqueConstraint('usename', name='user_usename_key'),
    postgresql_ignore_search_path=False
    )
    op.create_table('progress',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('course_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('progress_percentage', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['course.id'], name='progress_course_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='progress_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='progress_pkey')
    )
    op.create_table('course',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='course_pkey')
    )
    # ### end Alembic commands ###
