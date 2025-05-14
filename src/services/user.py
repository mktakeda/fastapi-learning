from fastapi import HTTPException

from src.database.config import database

class UserService:
    @staticmethod
    def get_user(id: int):
        user = database.get(id)
        if user is None:
            raise HTTPException(status_code=404, detail="NO USER FOUND")
        return {"name": user}

    @staticmethod
    def get_users():
        print(database)
        return {"database": database }

    @staticmethod
    def add_user(id: int,name: str):
        if id in database:
            raise HTTPException(status_code=400, detail="ID already taken")
        database[id] = name
        print(database)
        return {"message": "Record Inserted"}

    @staticmethod
    def update_user(id: int, name: str):
        if id not in database:
            raise HTTPException(status_code=400, detail="ID not found")
        database[id] = name
        print(database)
        return {"message": "Record Updated"}

    @staticmethod
    def delete_user(id: int):
        if id not in database:
            raise HTTPException(status_code=400, detail="ID not found")
        database.pop(id)
        print(database)
        return {"message": "Record Deleted"}

    @staticmethod
    def delete_users():
        database.clear()
        print(database)
        return {"message": "All Records Deleted"}

user = UserService()