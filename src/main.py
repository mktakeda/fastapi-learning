import uvicorn
from fastapi import FastAPI, HTTPException

app = FastAPI()

database = {1: "MANAV", 2: "SATVIK", 3: "TANMAY"}


@app.get("/health")
def get_healthg():
    return {"message": "Healthy"}


@app.get("/user/{id}")
def get_user(id: int):
    user = database.get(id)
    if user is None:
        raise HTTPException(status_code=404, detail="NO USER FOUND")
    return {"name": user}


@app.get("/{full_path:path}")
def get_default_msg(full_path: str):
    return {"message": f"DEFAULT PATH HIT for /{full_path}"}


def run_server():
    uvicorn.run("src.main:app", port=8000, reload=True)


if __name__ == "__main__":
    run_server()
