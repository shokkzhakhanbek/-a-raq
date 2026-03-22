"""create users shanyraks comments tables

Revision ID: acf2eaeded85
Revises:
Create Date: 2026-03-23 00:04:03.144723
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = 'acf2eaeded85'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("username", sa.String(), nullable=False, unique=True),
        sa.Column("phone", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("city", sa.String(), nullable=False),
    )

    op.create_table(
        "shanyraks",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("type", sa.String(), nullable=False),
        sa.Column("price", sa.Float(), nullable=False),
        sa.Column("address", sa.String(), nullable=False),
        sa.Column("area", sa.Float(), nullable=False),
        sa.Column("rooms_count", sa.Integer(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("user_id", sa.Integer(), sa.ForeignKey("users.id"), nullable=False),
    )

    op.create_table(
        "comments",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("content", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("author_id", sa.Integer(), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("shanyrak_id", sa.Integer(), sa.ForeignKey("shanyraks.id"), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("comments")
    op.drop_table("shanyraks")
    op.drop_table("users")