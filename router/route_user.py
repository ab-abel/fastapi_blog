from fastapi import APIRouter, HTTPException, status,Depends
from db.model.users import RegisterUser, LoginUser, Profile

from db.controller.users import registerUser, loginUser

from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session
from db.session import get_db

router = APIRouter()

@router.get('/')
async def index():
    pass

@router.get('/{id}')
async def show(id):
    pass

@router.post('/create')
def create(user: RegisterUser, db:Session =Depends(get_db)):
    user = registerUser.register(user, db)
    return user

@router.post('/login')
def login(user: OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm), db:Session=Depends(get_db)):
    # print(user.email)
    #to use OAuth change email to username
    user_login = loginUser.login(user, db)
    return user_login

@router.put('/{id}')
async def edit(id):
    pass

@router.delete('/{id}')
async def delete(id):
    pass

