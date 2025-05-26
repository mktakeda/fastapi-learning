from typing import List, Optional

import strawberry
from sqlalchemy.orm import Session

from src.graphql.schemas.types.user_type import UserType
from src.services.user import UserService
from src.utils.logger import logger


@strawberry.type
class Query:
    @strawberry.field
    def user(self, id: int, info) -> Optional[UserType]:
        logger.info(f"🔍 Fetching user with id={id}")
        db: Session = info.context.db
        user = UserService(db).get_user(id)
        logger.success(f"✅ Found user id={id}")
        return UserType(id=user["id"], name=user["name"])

    @strawberry.field
    def users(self, info) -> List[UserType]:
        logger.info("🔍 Fetching all users")
        db: Session = info.context.db
        result = UserService(db).get_users()
        logger.success(f"✅ Found {len(result['users'])} users")
        return [UserType(id=u["id"], name=u["name"]) for u in result["users"]]
