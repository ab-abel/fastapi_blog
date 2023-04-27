from fastapi import responses, status
from starlette.requests import Request
from core import cookie_auth
from typing import Optional

def logout(request: Request):
    resp = responses.RedirectResponse(url='/login', status_code=status.HTTP_302_FOUND)
    cookie_auth.unset_cookie(resp)
    return resp