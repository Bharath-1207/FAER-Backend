from fastapi import APIRouter, Depends
from app.core.security import validate_token

router = APIRouter()

@router.get("/secure-data", dependencies=[Depends(validate_token)])
def secure_data():
    return {"message": "Access granted. Secure data."}
