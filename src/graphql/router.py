from fastapi import Depends
from sqlalchemy.orm import Session
from strawberry.fastapi import GraphQLRouter

from src.database.dependency import get_db
from src.graphql.schemas.schema import Context, schema


async def get_context(db: Session = Depends(get_db)):
    return Context(db=db)


router = GraphQLRouter(schema, context_getter=get_context, tags=["GRAPHQL Methods"])
