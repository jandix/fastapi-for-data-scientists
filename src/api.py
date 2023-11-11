from fastapi import FastAPI
from pydantic import BaseModel

from database import Database

app = FastAPI()

database = Database(dataset="small")


# Create list endpoint including pagination using query parameters


# Create get by id endpoint using path parameters


# Create create endpoint using body parameters


# Create update endpoint using path and body parameters


# Create delete endpoint using path parameters
