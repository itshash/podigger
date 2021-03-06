"""empty message

Revision ID: a331c8728f7f
Revises: 094ef5ae04e9
Create Date: 2016-05-13 22:27:05.804402

"""

# revision identifiers, used by Alembic.
revision = 'a331c8728f7f'
down_revision = '094ef5ae04e9'

from alembic import op
import sqlalchemy as sa
from sqlalchemy_searchable import sync_trigger
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    conn = op.get_bind()
    op.add_column('episode', sa.Column('search_vector', sqlalchemy_utils.types.ts_vector.TSVectorType(), nullable=True))
    op.create_index('ix_episode_search_vector', 'episode', ['search_vector'], unique=False, postgresql_using='gin')
    sync_trigger(conn, 'episode', 'search_vector', ['title', 'description'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_episode_search_vector', table_name='episode')
    op.drop_column('episode', 'search_vector')
    ### end Alembic commands ###
