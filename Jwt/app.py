import os
from dotenv import load_dotenv
from Database.databaseConnection import engine, SessionLocal, Base

# internal imports
from Schema.formSchema import *
from Model.form import *
from Controller.formController import *

from fastapi import FastAPI, status, Response, Depends
from fastapi.middleware.cors import CORSMiddleware

from Authentication import auth


load_dotenv()


app = FastAPI(
    title="Jwt Form Service",
    version="0.0.1",
    description="FastAPI with Jwt Forms creation",
    openapi_tags=[
        {
            "name": "Home",
            "description": "Check health of the API"
        }
    ]
)

app.include_router(auth.router)


origins = ['http://localhost:8000', 'http://127.0.0.1:8000 ']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# routes
app.include_router(router, prefix="", tags=["Forms"])
