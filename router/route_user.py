from fastapi import APIRouter, HTTPException, status
from db.model.users import RegisterUser, LoginUser, Profile

router = APIRouter()

@router.get('/')
async def index():
    pass

@router.get('/{id}')
async def show(id):
    pass

@router.post('/create')
async def create():
    pass

@router.put('/{id}')
async def edit(id):
    pass

@router.delete('/{id}')
async def delete(id):
    pass

