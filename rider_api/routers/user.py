from fastapi import APIRouter, Depends,File,status,UploadFile,Form
from rider_api import schemas,oauth
from sqlalchemy.orm import Session
import database_connection
from rider_api.repository import user


router = APIRouter(
    prefix="/api/v1/user",
    tags=['Users']
    )

get_db = database_connection.get_db



@router.post('/',response_model=schemas.ShowUser )
async def user_create(
    full_name: str = Form(...),
    email: str = Form(...),
    phone_no: str = Form(...),
    user_type: int = Form(...),
    password: str = Form(...),
    vehicle: str = Form(...),
    is_active: bool = Form(None),
    is_block: bool = Form(None),
    avatar: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    user_data = schemas.User(
        full_name =full_name,
        email =email,
        phone_no =phone_no,
        user_type =user_type,
        password =password,
        vehicle =vehicle,
        is_active =is_active,
        is_block =is_block,
    )
    return await user.create(user_data,db,avatar)


@router.get('/details/{uuid}',response_model=schemas.ShowUser)

def singel_user_function(uuid:str,db:Session=Depends(get_db),current_user: schemas.User = Depends(oauth.get_current_user)):
    return user.single_user(uuid,db)

@router.put('/edit/{uuid}',status_code=status.HTTP_202_ACCEPTED )
async def user_edit(
    uuid:str,
    full_name: str = Form(...),
    email: str = Form(...),
    phone_no: str = Form(...),
    user_type: int = Form(...),
    password: str = Form(None),
    vehicle: str = Form(...),
    is_active: bool = Form(None),
    is_block: bool = Form(None),
    avatar: UploadFile = File(None),
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth.get_current_user)
):
    user_data = schemas.User(
        full_name =full_name,
        email =email,
        phone_no =phone_no,
        user_type =user_type,
        password =password,
        vehicle =vehicle,
        is_active =is_active,
        is_block =is_block,
    )
    return await user.create(user_data,db,avatar)







   
