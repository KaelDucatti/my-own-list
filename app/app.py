from http import HTTPStatus

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

from .schemas import MessageSchema, UserDB, UserList, UserPublic, UserSchema

app = FastAPI()


database = []


@app.get("/", status_code=HTTPStatus.OK, response_model=MessageSchema)
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.get("/hello/", status_code=HTTPStatus.OK, response_class=HTMLResponse)
def hello():
    return """
        <html>
        <head>
            <title>Hello</title>
        </head>
        <body>
            <h1>Hello</h1>
        </body>
        </html>
    """


@app.post("/users/", status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(
        **user.model_dump(),
        id=len(database) + 1,
    )
    database.append(user_with_id)
    return user_with_id


@app.get("/users/", status_code=HTTPStatus.OK, response_model=UserList)
def read_users():
    return {"users": database}


@app.put(
    "/users/{user_id}/", status_code=HTTPStatus.OK, response_model=UserPublic
)
def update_user(user: UserSchema, user_id: int):
    user = UserDB(
        **user.model_dump(),
        id=user_id,
    )
    try:
        database[user_id - 1] = user
    except IndexError:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="User not found",
        )
    return user


@app.delete(
    "/users/{user_id}/", status_code=HTTPStatus.OK, response_model=UserPublic
)
def delete_user(user_id: int):
    try:
        return database.pop(user_id - 1)
    except IndexError:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="User not found",
        )


@app.get(
    "/users/{user_id}/", status_code=HTTPStatus.OK, response_model=UserPublic
)
def detail_user(user_id: int):
    try:
        return database[user_id - 1]
    except IndexError:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="User not found",
        )
