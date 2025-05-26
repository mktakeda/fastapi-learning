from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.model.user import User
from src.utils.logger import logger


class UserService:
    def __init__(self, db: Session):
        self.db = db

    def get_user(self, id: int) -> dict:
        logger.info(f"🔍 Fetching user with ID {id}")
        user = self.db.query(User).filter(User.id == id).first()
        if user is None:
            logger.warning(f"❌ User with ID {id} not found")
            raise HTTPException(status_code=404, detail="NO USER FOUND")
        return {"id": user.id, "name": user.name}

    def get_users(self) -> dict:
        logger.info("📄 Fetching all users")
        users = self.db.query(User).all()
        return {"users": [{"id": user.id, "name": user.name} for user in users]}

    def add_user(self, id: int, name: str) -> dict:
        logger.info(f"➕ Adding user with ID {id}")
        if self.db.query(User).filter(User.id == id).first():
            logger.warning(f"⚠️ ID {id} already exists")
            raise HTTPException(status_code=400, detail="ID already taken")
        new_user = User(id=id, name=name)
        self.db.add(new_user)
        self.db.commit()
        logger.success(f"✅ User with ID {id} added")
        return {"message": "Record Inserted"}

    def update_user(self, id: int, name: str) -> dict:
        logger.info(f"🔄 Updating user with ID {id}")
        user = self.db.query(User).filter(User.id == id).first()
        if not user:
            logger.warning(f"❌ ID {id} not found for update")
            raise HTTPException(status_code=400, detail="ID not found")
        user.name = name  # type: ignore
        self.db.commit()
        logger.success(f"✅ User with ID {id} updated")
        return {"message": "Record Updated"}

    def delete_user(self, id: int) -> dict:
        logger.info(f"🗑️ Deleting user with ID {id}")
        user = self.db.query(User).filter(User.id == id).first()
        if not user:
            logger.warning(f"❌ ID {id} not found for deletion")
            raise HTTPException(status_code=400, detail="ID not found")
        self.db.delete(user)
        self.db.commit()
        logger.success(f"✅ User with ID {id} deleted")
        return {"message": "Record Deleted"}

    def delete_users(self) -> dict:
        logger.info("🗑️ Deleting all users")
        self.db.query(User).delete()
        self.db.commit()
        logger.success("✅ All user records deleted")
        return {"message": "All Records Deleted"}
