from sqlalchemy import Column, String, Integer
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from .database import Base


class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, nullable=False)  # The nullable constraint is just a precaution
    customer_name = Column(String, nullable=False)
    customer_password = Column(String, nullable=False)
    customer_email = Column(String, nullable=False, unique=True, index=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=True, server_default=text("now()"))
    # updated_at = Column(TIMESTAMP(timezone=True), nullable=True, server_onupdate=text("now()"))