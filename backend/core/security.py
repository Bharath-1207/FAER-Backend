import time
from fastapi import Header, HTTPException
from app.storage.token_store import get_token, delete_token

def validate_token(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Token missing")

    token_data = get_token(authorization)

    if not token_data:
        raise HTTPException(status_code=401, detail="Invalid token")

    if time.time() > token_data["expiry"]:
        delete_token(authorization)
        raise HTTPException(status_code=401, detail="Token expired")

    if token_data["uses_left"] <= 0:
        delete_token(authorization)
        raise HTTPException(status_code=401, detail="Token already used")
    

    # decrement usage
    token_data["uses_left"] -= 1
