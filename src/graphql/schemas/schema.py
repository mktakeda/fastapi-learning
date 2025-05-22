# WOULD COMBINE ALL THE MUTATIONS AND QUERRIES TO ONE SCHEMA
import strawberry

from src.graphql.schemas.resolvers.mutation_resolver import Mutation
from src.graphql.schemas.resolvers.query_resolver import Query

schema = strawberry.Schema(query=Query, mutation=Mutation)
