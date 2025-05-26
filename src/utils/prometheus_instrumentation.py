from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator


def setup_prometheus_instrumentation(app: FastAPI):
    Instrumentator().instrument(app).expose(app)
