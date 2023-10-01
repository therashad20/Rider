from fastapi import FastAPI
from rider_api.routers import authentication,app_functions,user
from rider_api import models
from fastapi.staticfiles import StaticFiles
from database_connection import engine
# import uvicorn

app = FastAPI(debug=True)


models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(user.router)

app.mount('/', StaticFiles(directory="all-upload-file"),name="images")

# if __name__ =="__main__":
#     uvicorn.run(app,host="127.0.0.1",port=8000)








