import uvicorn


def run_server():
    uvicorn.run("src.main:app", port=8000, reload=True)
