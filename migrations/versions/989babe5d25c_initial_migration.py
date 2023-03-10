"""initial migration

Revision ID: 989babe5d25c
Revises: 
Create Date: 2023-01-22 20:04:57.484647

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '989babe5d25c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('galleries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('photos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('path', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('gallery_items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('photo', sa.Integer(), nullable=True),
    sa.Column('gallery', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['gallery'], ['galleries.id'], name='fk_gallery_items_galleries_id_gallery'),
    sa.ForeignKeyConstraint(['photo'], ['photos.id'], name='fk_gallery_items_photos_id_photo'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('gallery_items')
    op.drop_table('photos')
    op.drop_table('galleries')
    # ### end Alembic commands ###
