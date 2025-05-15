import uvicorn


def run_server() -> None:
    uvicorn.run("src.main:app", port=8000, reload=True)
