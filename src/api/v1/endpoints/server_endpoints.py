from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def get_health() -> dict:
    return {"message": "Healthy"}


@router.get("/{full_path:path}")
def get_default_msg(full_path: str) -> dict:
    return {"message": f"DEFAULT PATH HIT for /{full_path}"}
