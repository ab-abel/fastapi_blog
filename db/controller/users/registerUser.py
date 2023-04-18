from db.model.users import RegisterUser 
from sqlalchemy.orm import Session
from db.schema.users import User
from core.pwd.hash import HashPassword
from fastapi import HTTPException

hashpwd = HashPassword()

def register(user: RegisterUser, db:Session):
    user_db_data = db.query(User).filter(
        User.email == user.email
    ).first()
    
    if user_db_data:
        raise HTTPException(status_code=400, detail="user already exist")
    user = User(
        firstname = user.firstname,
        lastname = user.lastname,
        email = user.email,
        password = hashpwd.create_hash(user.password),
        is_active = True
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

