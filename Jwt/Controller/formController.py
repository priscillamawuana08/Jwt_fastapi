from fastapi import APIRouter, Depends, HTTPException, status
from Model.form import *
from Schema.formSchema import UserBase
from typing import Annotated
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, async_session
from Database.databaseConnection import SessionLocal
import uuid
import logging
import os
from sqlalchemy import create_engine
from sqlalchemy import select
from fastapi.encoders import jsonable_encoder
from Authentication.auth import get_current_user


# Console Logging
log_level = logging.INFO
if os.environ.get('DEBUG'):
    log_level = logging.DEBUG

logging.basicConfig(filename="auth.log", level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s', datefmt='%d/%m/%Y %I:%M:%S%p')

logger = logging.getLogger(__name__)




async def get_db():
  
    db = SessionLocal()
    try:
        yield db

    finally:
       await db.close()

db_dependency = Annotated[async_session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]



router = APIRouter()


@router.post("/Users/create_user")
async def create_forms(user: UserBase, db: db_dependency):

    user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        password=user.password,
        username = user.username

    )

    async with db.begin():
        db.add(user)
        await db.commit()

    return {"message": "User  created successfully", "data":user}

@router.post("/user/", status_code=status.HTTP_200_OK)
async def user(db: db_dependency,user:user_dependency):
  if user is None:
      raise HTTPException(status_code = 401, details = 'Authentication failed')
  return {"User":user}
    
