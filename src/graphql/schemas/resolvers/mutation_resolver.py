import strawberry
from sqlalchemy.orm import Session

from src.services.user import UserService
from src.utils.logger import logger


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_user(self, id: int, name: str, info) -> str:
        logger.info(f"➕ Adding user with id={id} and name={name}")
        db: Session = info.context.db
        result = UserService(db).add_user(id, name)["message"]
        logger.success(f"✅ User added: id={id}")
        return result

    @strawberry.mutation
    def update_user(self, id: int, name: str, info) -> str:
        logger.info(f"✏️ Updating user id={id} to name={name}")
        db: Session = info.context.db
        result = UserService(db).update_user(id, name)["message"]
        logger.success(f"✅ User updated: id={id}")
        return result

    @strawberry.mutation
    def delete_user(self, id: int, info) -> str:
        logger.info(f"🗑️ Deleting user id={id}")
        db: Session = info.context.db
        result = UserService(db).delete_user(id)["message"]
        logger.success(f"✅ User deleted: id={id}")
        return result

    @strawberry.mutation
    def delete_all_users(self, info) -> str:
        logger.info("🗑️ Deleting all users")
        db: Session = info.context.db
        result = UserService(db).delete_users()["message"]
        logger.success("✅ All users deleted")
        return result
