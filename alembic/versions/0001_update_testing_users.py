""" 
Revision ID: 0000001
Revises: 00000000
"""

# revision identifiers, used by Alembic.
revision = '00000001'
down_revision = '00000000'

from alembic import op


def upgrade():
    op.execute('''UPDATE user SET point_balance = 1000 WHERE user_id = 1;''')
    op.execute('''UPDATE user SET tier = 'Silver' WHERE user_id = 3;''')


def downgrade():
    op.execute('''UPDATE user SET point_balance = 1 WHERE user_id = 1;''')
    op.execute('''UPDATE user SET tier = 'Carbon' WHERE user_id = 3;''')
