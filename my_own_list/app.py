from http import HTTPStatus

from fastapi import FastAPI

from my_own_list.schemas import (
    Message,
    UserDB,
    UserPrivateSchema,
    UserPublicSchema,
)

app = FastAPI(title="My-Own-List")

database = []


@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message": "Hello, FastAPI"}


@app.post(
    "/users/", status_code=HTTPStatus.CREATED, response_model=UserPublicSchema
)
def create_user(user: UserPrivateSchema):
    new_user = UserDB(id=len(database) + 1, **user.model_dump())
    database.append(new_user)
    return user


@app.get("/users/", status_code=HTTPStatus.OK, response_model=UserPublicSchema)
def list_users(): ...
