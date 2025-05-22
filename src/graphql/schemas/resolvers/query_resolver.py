from typing import List, Optional

import strawberry
from sqlalchemy.orm import Session

from src.graphql.schemas.types.user_type import UserType
from src.services.user import UserService


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
