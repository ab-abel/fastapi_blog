from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from core.token.token_handler import verify_access_token


outh2_scheme = OAuth2PasswordBearer(tokenUrl='/users/login')

async def authenticate(token:str = Depends(outh2_scheme))->str:
    if not token:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
        detail="Sign in for access"
        )
    decode_token = verify_access_token(token)
    # return decode_token["user"]
    return decode_token["user"]