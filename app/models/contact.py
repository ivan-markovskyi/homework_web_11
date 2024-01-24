from sqlalchemy import Column, String, Boolean, DateTime

from .base import BaseModel, Base


class ContactDB(BaseModel):
    __tablename__ = "contacts"

    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone_number = Column(String)
    birthday = Column(String)
    description = Column(String)
