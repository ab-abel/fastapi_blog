from db.model.users import Profile, ChangePassword, ForgetPassword
from sqlalchemy.orm import Session
from db.schema.users import User
from core.pwd.hash import HashPassword
from fastapi import HTTPException


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

    hashpwd =HashPassword()

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