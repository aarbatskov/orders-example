import sqlalchemy as sa
from sqlalchemy import MetaData, func
from sqlalchemy.dialects.postgresql import UUID

meta = MetaData()


orders = sa.Table(
    "orders",
    meta,
    sa.Column("id", UUID, primary_key=True, server_default=func.gen_random_uuid()),
    sa.Column("user_id", UUID, nullable=False),
    sa.Column("comment", sa.String(), nullable=True),
    sa.Column("total_price", sa.Float()),
    sa.Column(
        "created_at",
        sa.DateTime(timezone=True),
        server_default=sa.func.current_timestamp(),
        nullable=False,
    ),
    sa.Column(
        "updated_at",
        sa.DateTime(timezone=True),
        server_default=sa.func.current_timestamp(),
        nullable=False,
    ),
)
