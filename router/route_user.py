from fastapi import APIRouter, HTTPException, status,Depends, requests
from db.model.users import *

from db.controller.users import registerUser, loginUser, logoutUser, userController

from fastapi.security import OAuth2PasswordRequestForm

from starlette.requests import Request
from core.auth import authenticate

from sqlalchemy.orm import Session
from db.session import get_db


router = APIRouter()

@router.get('/')
def index(db:Session =Depends(get_db)):
    result = userController.get_all_users(db)
    return result

@router.get('/{id}')
def show(id: int = Depends(authenticate), db:Session= Depends(get_db)):
    user = userController.get_user_id(id, db)
    return user

@router.post('/create')
def create(user: RegisterUser, db:Session =Depends(get_db)):
    user = registerUser.register(user, db)
    return user

@router.post('/login')
def login(user: OAuth2PasswordRequestForm = Depends(), db:Session=Depends(get_db)):
    # print(user.email)
    #to use OAuth change email to username
    user_login = loginUser.login(user, db)
    return user_login

@router.post('/logout')
def logout(request: Request):
    logoutUser.logout(request)

# : int = Depends(authenticate)
# , 
@router.put('/{id}',response_model=Profile)
async def edit(id : int, user: Profile,  db:Session =Depends(get_db)):
    user_exist = userController.get_user_id(id, db)
    if not user_exist:
        raise HTTPException(status_code=404, detail="user with user id: {id} does not exist")
    user = userController.edit_user(id, user, db)
    return user

# = Depends(authenticate)
@router.delete('/{id}')
async def delete(id : int= Depends(authenticate), db:Session =Depends(get_db)):
    delete_user = userController.user_delete(id, db)
    if not delete_user:
        raise HTTPException(status_code=404,
        detail="User does not exist")
    return delete_user


@router.patch('/change_password')
def change_user_pwd(update_password:ChangePassword, db:Session = Depends(get_db), current_user:int = Depends(authenticate)):
    change_pwd = userController.change_password(current_user, update_password, db)

    if not change_pwd:
        raise HTTPException(status_code=404, detail="change password not successful")

@router.post('/forget_password')
def forget_pwd(user:ForgetPassword, request:Request, db:Session=Depends(get_db)):
    user_login = userController.forget_pwd(user, request, db)
    # return user_login

@router.patch('/forget_password/{token}')
def reset_password(token, user:ResetPassword, db:Session = Depends(get_db)):
    #TODO: Verify token
    reset_user_details = userController.reset_pwd(token, user, db)
    return reset_user_details