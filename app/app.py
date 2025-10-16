from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from .schemas import Message, UserSchema

app = FastAPI()


@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.get("/hello", status_code=HTTPStatus.OK, response_class=HTMLResponse)
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


@app.post("/users/")
def create_user(user: UserSchema):
    return user
