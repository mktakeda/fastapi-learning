from fastapi import Depends
from sqlalchemy.orm import Session
from strawberry.fastapi import BaseContext

from src.database.dependency import get_db


# Strawberry GraphQL Context
class Context(BaseContext):
    def __init__(self, db: Session):
        self.db = db


async def get_context(db: Session = Depends(get_db)):
    return Context(db=db)
