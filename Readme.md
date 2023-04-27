# Simple FastAPI Blog #

### Overview
This is a simple blog backend project, using fastapi. the backend to the blog site being PostgreSQL server. 

## Features in brief
1. login
2. Change Password
3. Register
4. Login
5. create Post
6. view Post
7. comment features.


## Architecture

- core
    - pwd 
        - hash.py
    - token
        -token_handler.py
    - auth.py
    - config.py
    - cookie_auth.py
- db
    - controller
        - users
            - loginUser.py
            - logoutUser.py
            - registerUser.py
            - userController.py
        - model
            - users.py
        - schema 
             users.py
        - base.py
        - db_base.py
        - session.py
- router
    - base.py
    - route_user.py

- test
- env.example
- main.py
- requirements.txt
- Readme.md

## Routing Overview
when a user request a url, the APIRouter model handels the route and make a call to the controller with in turn get the requires infomation from the database. 




<!-- 
async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user
@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)): 
    return current_user
    
    -->