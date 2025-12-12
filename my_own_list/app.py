from http import HTTPStatus

from fastapi import FastAPI

from my_own_list.schemas import Message, UserPrivateSchema, UserPublicSchema

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello, FastAPI'}


@app.post(
    '/user/', status_code=HTTPStatus.CREATED, response_model=UserPublicSchema
)
def create_user(user: UserPrivateSchema):
    return user
