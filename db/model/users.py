from pydantic import BaseModel, EmailStr

class RegisterUser(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    password: str

    class config:
        schema_extra = {
            'example':{
                'firstname':'John',
                'lastname':'Doe',
                'email':'John.doe@johndoe.com',
                'password':'str12345'
            }
        }

class LoginUser(BaseModel):
    email:EmailStr
    password: str

class Profile(BaseModel):
    firstname: str
    lastname: str
    # email: EmailStr
    # is_active: bool

    class config:
        orm_mode = True
    
class ForgetPassword(BaseModel):
    oldPassword: str
    newPassword: str
    confirmPassword: str

class ChangePassword(BaseModel):
    oldPassword: str
    newPassword: str
    confirmPassword:str