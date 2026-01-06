from fastapi import FastAPI
from app.api import token, protected

app = FastAPI(title="GuardianToken Backend")

app.include_router(token.router, prefix="/token")
app.include_router(protected.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "GuardianToken backend running"}