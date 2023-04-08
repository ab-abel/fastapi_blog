from db.model.users import RegisterUser 
from sqlalchemy.orm import Session
from db.schema.users import User
from core.pwd.hash import HashPassword

hashpwd = HashPassword()

def register(user: RegisterUser, db:Session):
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

