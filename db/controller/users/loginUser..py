from db.model.users import LoginUser
from sqlalchemy.orm import Session
from db.schema.users import User

def login(user: LoginUser, db:Session):
    #TODO: check Db for user credentials
    #TODO: compare both provided and suppied,
    #TODO: create a token

    user = User(
        email = user.email,
        password = user.password,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
