from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def get_health():
    return {"message": "Healthy"}


@router.get("/{full_path:path}")
def get_default_msg(full_path: str):
    return {"message": f"DEFAULT PATH HIT for /{full_path}"}
