from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from src.utils.logger import logger


def setup_prometheus_instrumentation(app: FastAPI):
    logger.info("🔧 Setting up Prometheus instrumentation")
    try:
        Instrumentator().instrument(app).expose(app)
        logger.success("✅ Prometheus metrics exposed at /metrics")
    except Exception as e:
        logger.exception(f"❌ Failed to set up Prometheus instrumentation: {e}")
