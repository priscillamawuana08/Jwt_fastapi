from sqlalchemy import Boolean, Column, Integer, String, UUID, DateTime, func, ARRAY, text
from Database.databaseConnection import Base
import datetime
# from typing import List


class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text(
        "uuid_generate_v4()"), unique=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    username = Column(String, nullable=False, unique=True)
    created_on = Column(DateTime, nullable=False,
                        default=func.current_timestamp())


class Auth(Base):
    __tablename__ = 'login'


    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text(
        "uuid_generate_v4()"), unique=True, index=True)
    username = Column(String, nullable=False)
    password = Column(String)
