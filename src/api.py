from typing import Annotated

from fastapi import Body, FastAPI, Path, Query
from pydantic import BaseModel
from starlette import status

from database import Database, NutsStatistic

app = FastAPI()

database = Database(dataset="large")


# Create list endpoint including pagination using query parameters
class ReadNutsStatistic(BaseModel):
    nuts_id: str
    total_jobs: int
    total_jobs_per_10k: float


@app.get(path="/", response_model=list[ReadNutsStatistic])
def list(
    page: Annotated[int, Query(...)],
    limit: Annotated[int, Query(...)],
) -> list[NutsStatistic]:
    return database.list()[(page - 1) * limit : page * limit]


# Create get by id endpoint using path parameters
@app.get(path="/{id}", response_model=ReadNutsStatistic)
def get_by_id(id: Annotated[str, Path(...)]) -> NutsStatistic:
    return database.get_by_id(id)


# Create create endpoint using body parameters
class CreateNutsStatistic(BaseModel):
    nuts_id: str
    total_jobs: int
    total_jobs_per_10k: float


@app.post(path="/", response_model=ReadNutsStatistic)
def create(
    nuts_statistics: Annotated[CreateNutsStatistic, Body(...)],
) -> NutsStatistic:
    return database.create(nuts_statistics.model_dump())


# Create update endpoint using path and body parameters
class UpdateNutsStatistic(BaseModel):
    nuts_id: str
    total_jobs: int
    total_jobs_per_10k: float


@app.patch(path="/{id}", response=ReadNutsStatistic)
def update(
    id: Annotated[str, Path(...)],
    nuts_statistics: Annotated[UpdateNutsStatistic, Body(...)],
) -> NutsStatistic:
    database.update(id, nuts_statistics.model_dump())
    return database.get_by_id(id)


# Create delete endpoint using path parameters
@app.delete(path="/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    id: Annotated[str, Path(...)],
) -> None:
    return database.delete(id)
