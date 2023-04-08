from fastapi import HTTPException, status, Depends, Response

from db.model.users import LoginUser
from sqlalchemy.orm import Session
from db.schema.users import User
from core.pwd.hash import HashPassword
from core.token.token_handler import create_access_token

hashpwd = HashPassword()
def login(user: LoginUser, db:Session):
# def login(user: OAuth2PasswordRequestForm, db:Session):
    user_exist = db.query(User).filter(User.email == user.username).scalar()
    if not user_exist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Email does not exist"
        )

    if hashpwd.verify_hash(user.password, user_exist.password):
        access_token = create_access_token(user_exist.email)
        #TODO set cookie

        return{
                "access_token": access_token,
                "token_type":"Bearer"
        }
    else: 
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail="Wrong password")
    
    raise HTTPException(
        status_code = status.HTTP_200_OK,
        detail="login successful"
        )
    # return user_exist