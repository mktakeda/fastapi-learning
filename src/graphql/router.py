from strawberry.fastapi import GraphQLRouter

from src.graphql.context import get_context
from src.graphql.schemas.schema import schema

router = GraphQLRouter(schema, context_getter=get_context, tags=["GRAPHQL Methods"])
