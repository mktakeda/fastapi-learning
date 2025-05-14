from typing import Optional

import uvicorn
from fastapi import APIRouter, FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
router = APIRouter()

# -------------------DATABASE-----------------------------
database = {1: "MANAV", 2: "SATVIK", 3: "TANMAY"}


# ------------------MODELS-------------------------------
class User(BaseModel):
    id: int
    name: str
    discription: Optional[str] = None


# -------------------ENDPOINTS----------------------------


@router.get("/health")
def get_health():
    return {"message": "Healthy"}


@router.get("/user/{id}")
def get_user(id: int):
    user = database.get(id)
    if user is None:
        raise HTTPException(status_code=404, detail="NO USER FOUND")
    return {"name": user}


@router.get("/users")
def get_users():
    return {"database": database}


@router.get("/{full_path:path}")
def get_default_msg(full_path: str):
    return {"message": f"DEFAULT PATH HIT for /{full_path}"}


@router.post("/user")
def add_user(payload: User):
    if payload.id in database:
        raise HTTPException(status_code=400, detail="ID already taken")
    database[payload.id] = payload.name
    print(database)
    return {"message": "Record Inserted"}


@router.put("/user/{id}")
def update_user(id: int, payload: User):
    if id not in database:
        raise HTTPException(status_code=400, detail="ID not found")
    database[id] = payload.name
    print(database)
    return {"message": "Record Updated"}


@router.delete("/user/{id}")
def delete_user(id: int):
    if id not in database:
        raise HTTPException(status_code=400, detail="ID not found")
    database.pop(id)
    print(database)
    return {"message": "Record Deleted"}


@router.delete("/users")
def delete_users():
    database.clear()
    print(database)
    return {"message": "All Records Deleted"}


# -----------------------ROUTER--------------------
app.include_router(router, prefix="/api/v1")


# -----------------------SERVER--------------------
def run_server():
    uvicorn.run("src.main:app", port=8000, reload=True)


if __name__ == "__main__":
    run_server()
