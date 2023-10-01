from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from rider_api import schemas, models, token,JWTtoken
from rider_api.hashing import Hash
from sqlalchemy.orm import Session
import database_connection  


router = APIRouter(
    prefix="/api/v1/auth/login",
    tags=['Auth']
    )

get_db = database_connection.get_db


@router.post('/')
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.email==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid Credentials")
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Incorrect password")
    
    access_token =JWTtoken.create_access_token(data={"sub": user.email})
    return {"access_token":access_token,"token_type":"bearer"}