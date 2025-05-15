from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.model.user import User


class UserService:
    def __init__(self, db: Session):
        self.db = db

    def get_user(self, id: int) -> dict:
        user = self.db.query(User).filter(User.id == id).first()
        if user is None:
            raise HTTPException(status_code=404, detail="NO USER FOUND")
        return {"id": user.id, "name": user.name}

    def get_users(self) -> dict:
        users = self.db.query(User).all()
        return {"users": [{"id": user.id, "name": user.name} for user in users]}

    def add_user(self, id: int, name: str) -> dict:
        if self.db.query(User).filter(User.id == id).first():
            raise HTTPException(status_code=400, detail="ID already taken")
        new_user = User(id=id, name=name)
        self.db.add(new_user)
        self.db.commit()
        return {"message": "Record Inserted"}

    def update_user(self, id: int, name: str) -> dict:
        user = self.db.query(User).filter(User.id == id).first()
        if not user:
            raise HTTPException(status_code=400, detail="ID not found")
        user.name = name
        self.db.commit()
        return {"message": "Record Updated"}

    def delete_user(self, id: int) -> dict:
        user = self.db.query(User).filter(User.id == id).first()
        if not user:
            raise HTTPException(status_code=400, detail="ID not found")
        self.db.delete(user)
        self.db.commit()
        return {"message": "Record Deleted"}

    def delete_users(self) -> dict:
        self.db.query(User).delete()
        self.db.commit()
        return {"message": "All Records Deleted"}
