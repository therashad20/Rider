
from secrets import token_hex
from fastapi import UploadFile,File

async def file_or_image_upload(IMAGEDIR:str, file:UploadFile = File(None)):
    
    file_ext = file.filename.split(".")[-1]
    file_name = token_hex(30)
    file_path = f"{IMAGEDIR}/{file_name}.{file_ext}"
    file_save_path =f"{file_name}.{file_ext}"
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
    return file_save_path








