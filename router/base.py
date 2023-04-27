from fastapi import APIRouter

from router import route_user 

router = APIRouter()

router.include_router(route_user.router, prefix='/users', tags=['users'])



