"""empty message

Revision ID: 2298408681b6
Revises: a92893ddf493
Create Date: 2016-04-24 15:41:05.870000

"""

# revision identifiers, used by Alembic.
revision = '2298408681b6'
down_revision = 'a92893ddf493'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('podcast_feed_key', 'podcast', type_='unique')
    op.drop_constraint('podcast_name_key', 'podcast', type_='unique')
    op.add_column('tag', sa.Column('name', sa.String(), nullable=False))
    op.create_index(op.f('ix_tag_name'), 'tag', ['name'], unique=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tag_name'), table_name='tag')
    op.drop_column('tag', 'name')
    op.create_unique_constraint('podcast_name_key', 'podcast', ['name'])
    op.create_unique_constraint('podcast_feed_key', 'podcast', ['feed'])
    ### end Alembic commands ###
