import strawberry
from sqlalchemy.orm import Session

from src.services.user import UserService


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
