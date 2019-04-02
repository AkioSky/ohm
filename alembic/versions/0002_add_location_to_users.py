"""
Revision ID: 0000002
Revises: 0000001
"""

# revision identifiers, used by Alembic.
revision = '00000002'
down_revision = '00000001'

from alembic import op


def upgrade():
    op.execute('''ALTER TABLE user
        ADD COLUMN location VARCHAR(3) DEFAULT NULL;''')
    op.execute('''UPDATE user SET location = 'USA' WHERE user_id = 2;''')


def downgrade():
    op.execute('''ALTER TABLE user
        DROP COLUMN location;''')
