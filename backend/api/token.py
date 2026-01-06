from fastapi import APIRouter
import secrets
from backend.storage.token_store import create_token

router = APIRouter()

@router.post("/generate")
def generate_token():
    token = secrets.token_urlsafe(16)

    ttl = 60        # seconds
    max_uses = 1    # one‑time token

    create_token(token, ttl, max_uses)

    return {
        "token": token,
        "expires_in": ttl,
        "max_uses": max_uses
    }