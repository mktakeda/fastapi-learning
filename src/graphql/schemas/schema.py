from typing import List, Optional

import strawberry
from sqlalchemy.orm import Session
from strawberry.fastapi import BaseContext

from src.services.user import UserService


# Strawberry GraphQL Context
class Context(BaseContext):
    def __init__(self, db: Session):
        self.db = db


@strawberry.type
class UserType:
    id: int
    name: str


@strawberry.type
class Query:
    @strawberry.field
    def user(self, id: int, info) -> Optional[UserType]:
        db: Session = info.context.db
        user = UserService(db).get_user(id)
        return UserType(id=user["id"], name=user["name"])

    @strawberry.field
    def users(self, info) -> List[UserType]:
        db: Session = info.context.db
        result = UserService(db).get_users()
        return [UserType(id=u["id"], name=u["name"]) for u in result["users"]]


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_user(self, id: int, name: str, info) -> str:
        db: Session = info.context.db
        return UserService(db).add_user(id, name)["message"]

    @strawberry.mutation
    def update_user(self, id: int, name: str, info) -> str:
        db: Session = info.context.db
        return UserService(db).update_user(id, name)["message"]

    @strawberry.mutation
    def delete_user(self, id: int, info) -> str:
        db: Session = info.context.db
        return UserService(db).delete_user(id)["message"]

    @strawberry.mutation
    def delete_all_users(self, info) -> str:
        db: Session = info.context.db
        return UserService(db).delete_users()["message"]


schema = strawberry.Schema(query=Query, mutation=Mutation)
