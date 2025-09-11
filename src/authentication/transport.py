from fastapi_users.authentication import BearerTransport

from src.config import settings


bearer_transport = BearerTransport(
    #TODO: update url
    tokenUrl="auth/login",#settings.bearer_token_url,
)
