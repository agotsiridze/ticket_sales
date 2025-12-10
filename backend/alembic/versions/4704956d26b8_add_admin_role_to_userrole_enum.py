"""add admin role to userrole enum

Revision ID: 4704956d26b8
Revises: 912d84fff472
Create Date: 2025-12-10 23:27:48.810891

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4704956d26b8'
down_revision: Union[str, None] = '912d84fff472'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("ALTER TYPE userrole ADD VALUE IF NOT EXISTS 'admin'")
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
