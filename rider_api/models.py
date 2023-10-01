from sqlalchemy import Column, Integer, DateTime, String, ForeignKey, Boolean,Float,Double,Text,Index
from database_connection import Base
from sqlalchemy.orm import relationship
from base_uuid_models.uuid_models import Uuid_models


# class Package(Uuid_models):

#     __tablename__='packages'

#     id = Column(Integer, primary_key=True, index=True)
#     pack_name = Column(String, nullable=False)
#     info = Column(Text, nullable=False)
#     facility =Column(Text,nullable=False)
#     price =Column(Double,nullable=False)
#     validity=Column(String,nullable=False)

#     # shope_details = relationship("Shope", back_populates="package_details")

# class Shope(Uuid_models):

#     __tablename__ = 'shopes'

#     id = Column(Integer, primary_key=True, index=True)
#     shop_name = Column(String, nullable=False)
#     email = Column(String, unique=True, nullable=False)
#     phone_no = Column(String, unique=True, nullable=False)
#     shope_type = Column(String,nullable=False)
#     delivery_range = Column(Integer,nullable=False)
#     address = Column(String,nullable=False)
#     lat = Column(String,nullable=False)
#     lng = Column(String,nullable=False)
#     is_active = Column(Boolean, default=True,nullable=False)
#     is_block= Column(Boolean, default=False,nullable=False)
#     avater = Column(String, unique=True, nullable=True)
#     admin_comm = Column(Double,nullable=True)
#     subcrip_package = Column(String, ForeignKey('packages.uuid'), nullable=True)
#     description = Column(Text,nullable=True)
#     info = Column(Text,nullable=True)
#     users_details = relationship("User", back_populates="shop_details")
 
class User(Uuid_models):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(245), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    phone_no = Column(String(255), unique=True, nullable=False)
    vehicle = Column(String(255), unique=True, nullable=False)
    user_type = Column(Integer, default=1, nullable=False)
    # shope_id = Column(String, ForeignKey('shopes.uuid'), nullable=True)
    avatar = Column(String(255), unique=True, nullable=True)
    is_active = Column(Boolean, default=True,nullable=False)
    is_block= Column(Boolean, default=False,nullable=False)
    password = Column(String(255),nullable=False)
    
    # shop_details = relationship("Shope", foreign_keys=[shope_id], back_populates="users_details")





  
