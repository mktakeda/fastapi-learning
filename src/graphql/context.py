from fastapi import Depends
from sqlalchemy.orm import Session
from strawberry.fastapi import BaseContext

from src.database.dependency import get_db
from src.utils.logger import logger


# Strawberry GraphQL Context
class Context(BaseContext):
    def __init__(self, db: Session):
        logger.info("📚 Initializing GraphQL context with DB session")
        self.db = db


async def get_context(db: Session = Depends(get_db)):
    logger.info("🔗 Creating GraphQL context dependency")
    return Context(db=db)
