import os

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
# AsyncSession
from sqlalchemy.orm import sessionmaker, DeclarativeBase

db_user = "postgres"
db_pass = "asdf"
db_host = "localhost:5432"
db_name = "Jwt"


SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{db_user}:{db_pass}@{db_host}/{db_name}"


engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)


# SessionLocal = sessionmaker(expire_on_commit=False,
#                             class_=AsyncSession, bind=engine)

SessionLocal = async_sessionmaker(
    autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


async def create_database_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# Use asyncio to run the asynchronous setup code
async def setup():
    await create_database_tables()
