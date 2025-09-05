import secrets
import uuid
from time import time
from typing import Annotated, Any
from fastapi import APIRouter, HTTPException, Response, Depends, status, Header, Cookie
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel

log_router = APIRouter(prefix="/auth", tags=["Авторизация"])

security = HTTPBasic()


@log_router.get("/basic_auth/")
async def auth_credentials(
        credentials: Annotated[HTTPBasicCredentials, Depends(security)],
):
    return {"message": "Hi",
            "username": credentials.username,
            "password": credentials.password,
            }


usernames_to_passwords = {
    "admin": "admin",
    "root": "root",
}


static_auth_token_to_username = {
    "a2098667b72590ca3d65c3ee66266163": "admin",
    "12d7c363a1141db91a573e39aaea1111": "root",
}


async def get_auth_user_username(
        credentials: Annotated[HTTPBasicCredentials, Depends(security)]
) -> str:
    unauthed_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password",
        headers={"WWW-Authenticate": "Basic"},
    )
    correct_password = usernames_to_passwords.get(credentials.username)
    if correct_password is None:
        raise unauthed_exc

    if not secrets.compare_digest(
            credentials.password.encode("utf-8"),
            correct_password.encode("utf-8"),
    ):
        raise unauthed_exc

    return credentials.username


async def get_username_by_static_auth_token(
        static_token: str = Header(alias="x-auth-token"),
) -> str:
    if username := static_auth_token_to_username.get(static_token):
        return username

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="token invalid",
    )


@log_router.get("/basic_auth-username/")
async def auth_user(
        auth_username: str = Depends(get_auth_user_username),
):
   return {
       "message": f"Hi, {auth_username}!",
       "username": auth_username,
   }


@log_router.get("/http-header-auth/")
async def auth_http_header(
        auth_username: str = Depends(get_username_by_static_auth_token),
):
   return {
       "message": f"Hi, {auth_username}!",
       "username": auth_username,
   }


COOKIES: dict[str, dict[str, Any]] = {}
COOKIE_SESSION_ID_KEY = "web-app-session-id"


def generate_session_id() -> str:
    return uuid.uuid4().hex


def get_session_data(
        session_id: str = Cookie(alias=COOKIE_SESSION_ID_KEY),
):
    if session_id not in COOKIES:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="not authenticated",
        )
    return COOKIES[session_id]


@log_router.post("/login-cookie/")
async def login_cookie(
        response: Response,
        auth_username: str = Depends(get_auth_user_username),
        #auth_username: str = Depends(get_username_by_static_auth_token),
):
    session_id = generate_session_id()
    COOKIES[session_id] = {
        "username": auth_username,
        "login_at": int(time()),
    }
    response.set_cookie(COOKIE_SESSION_ID_KEY, session_id)
    return {"result": "ok"}


@log_router.get("/check-cookie/")
async def auth_check_cookie(
        user_session_data: dict = Depends(get_session_data),
):
    username = user_session_data["username"]
    return {
        "username": f"Hello, {username}!",
        **user_session_data,
    }


@log_router.get("/logout-cookie/")
async def auth_logout_cookie(
        response: Response,
        session_id: str = Cookie(alias=COOKIE_SESSION_ID_KEY),
        user_session_data: dict = Depends(get_session_data),
):
    COOKIES.pop(session_id)
    response.delete_cookie(COOKIE_SESSION_ID_KEY)
    username = user_session_data["username"]
    return {
        "username": f"Bye, {username}!",
    }
