import secrets
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.staticfiles import StaticFiles
from fastapi.security import HTTPBasic, HTTPBasicCredentials


api_app = FastAPI(title="api")
app = FastAPI(title="main app")
security = HTTPBasic()

@app.get("/health")
async def health():
    return {"message":"ok"}

@app.get("/users/me")
def read_current_user(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    return {"username": credentials.username, "password": credentials.password}

app.mount("/api", api_app)
app.mount("/", StaticFiles(directory="ui", html=True), name="ui")

