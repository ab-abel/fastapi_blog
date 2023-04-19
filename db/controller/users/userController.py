from db.model.users import Profile, ChangePassword, ForgetPassword
from sqlalchemy.orm import Session
from db.schema.users import User
from core.pwd.hash import HashPassword
from fastapi import HTTPException, Request

from core.token import token_handler
from core.config import settings
import yagmail


def get_all_users(db: Session):    
    result = db.query(User).all()
    return result

def get_user_id(id: int, db:Session):
    result = db.query(User).get(id)

    return result


def edit_user(id: int, user:Profile, db:Session):
    # result = get_user_id(id, db)
    result = db.query(User).filter(User.id == id)
    user_result = result.first()
    if not user_result:
       raise HTTPException(status_code=404, details="User not found")
    user_dict = user.dict(exclude_unset=True)
    # print(user_dict)

    result.update(
        user_dict, synchronize_session =False
    )
     
    db.commit()
    db.refresh(user_result)
    return user_result


def user_delete(id: int, db:Session):
    delete_user = db.query(User).filter(
        User.id == id).first()
    
    if not delete_user:
       raise HTTPException(status_code= 404, detail="Users does not exist") 
    db.delete(delete_user)
    db.commit()
    return {"message": "successful deleted"}

def change_password(auth_user_email, update_password:ChangePassword, db:Session):
    user_exist = db.query(User).filter(User.email == auth_user_email)

    get_current_user = user_exist.first()

    # print(auth_user)
    # print(get_current_user.id)

    if get_current_user.email != auth_user_email:
        raise HTTPException(status_code=403, detail="not authorized")
    
    # #TODO: check old pass

    hashpwd = HashPassword()

    # print(get_current_user.password)
    # print(update_password.oldPassword)

    if not hashpwd.verify_hash(update_password.oldPassword, get_current_user.password):
        raise HTTPException(status_code=400, detail="Your old password is incorrect")
    
    # if update_password.oldPassword != update_password.confirmPassword:
    #     raise HTTPException(status_code=400, details="Your password must match")

    update_password = hashpwd.create_hash(update_password.newPassword)

    user_exist.update({
        'password':str(update_password)
    }, synchronize_session=False)
    db.commit()

    raise HTTPException(status_code=200, detail="Password updated successful")
    return {
        'message': 'Password change successful'
    }

def forget_pwd(user_email, request, db:Session):

    user_exist = db.query(User).filter(User.email == user_email.email)
    user_detail = user_exist.first()    
    if user_detail is None:
        raise HTTPException(
            status_code=404,
            detail=f"Email:{user_email.email}  does not exist"
        )
    token = token_handler.create_access_token(user_email.email)
    url = request.url._url+'/'+token
    # print(token)
    # print(request.url._url+'/'+token)
    # print(url)
    send_mail = send_reset_mail(user_email.email, url)
    return {
        "message":"message sent successfully",
        "data":send_mail
    }

def send_reset_mail(user_email, url):
    msg = f'''
    TO reset your password visit the link below:
    {url} 
    if you recive this email by error simply ignore.
    '''
    # print(user_email)
    try:
        #initialize server connection
        yag = yagmail.SMTP(user=settings.SMTP_user, password=settings.SMTP_pwd)
        #send_email
        yag.send(to=user_email, subject="Password Reset Request", content=msg)
        return {
            "message":"message sent succesfully"
        }
    except:
        return {
            "message":"Error sending mail"
        }


def reset_pwd(token, user_data, db:Session):
    check_token = token_handler.verify_access_token(token)['user']
    # print(check_token)
    if not check_token:
        raise HTTPException(status_code=404, detail="wrong url")
    user_exist = db.query(User).filter(User.email == check_token)
    user_detail = user_exist.first()
    # print(user_detail)
    hashpwd = HashPassword()
    if user_detail:
        pwd_hash = hashpwd.create_hash(user_data.newPassword)
    #     # user_exist.update({password : pwd_hash})
        user_detail.password = pwd_hash
        db.commit()
        raise HTTPException(status_code=200, detail="successful")
        return {
            "message":"success", 'alert':'success'
        }
    else:
        raise HTTPException(status_code=404, detail="password update not succesful")

