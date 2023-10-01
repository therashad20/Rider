
from sqlalchemy.orm import Session
from rider_api import models, schemas
from fastapi import UploadFile, File,HTTPException,status
from file_upload_traite.file_upload import file_or_image_upload
from rider_api.hashing import Hash


async def create(request: schemas.User, db: Session, file: UploadFile):
    
    if file:
        file_path = await file_or_image_upload('all-upload-file', file)
    else: 
        file_path = None
    user_data = models.User(
        full_name=request.full_name,
        avatar=file_path,
        email=request.email,
        phone_no=request.phone_no,
        vehicle=request.vehicle,
        is_active=request.is_active,
        password=Hash.bcrypt(request.password)
    )
    db.add(user_data)
    db.commit()
    db.refresh(user_data)
    return user_data


def single_user(uuid,db:Session):
    user=db.query(models.User).filter(models.User.uuid==uuid).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the {uuid} is not available")
    return user



