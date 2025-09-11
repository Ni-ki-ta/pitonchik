from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer

from dependencies.backend import authentication_backend
from routers.shemas.user import UserRead, UserCreate
from src.fastapi_users_rout import fastapi_users

http_bearer = HTTPBearer(auto_error=False)

auth_router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
    dependencies=[Depends(http_bearer)]
)

# /logout
# /login
auth_router.include_router(
    router=fastapi_users.get_auth_router(
        authentication_backend,
        # requires_verification=True
    ),

)

# /register
auth_router.include_router(
    router=fastapi_users.get_register_router(UserRead, UserCreate)
)

# /request-verify-token
# /verify
auth_router.include_router(
    router=fastapi_users.get_verify_router(UserRead)
)

# /forgot-password
# /reset-password
auth_router.include_router(
    router=fastapi_users.get_reset_password_router()
)
