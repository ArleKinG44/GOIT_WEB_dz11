from datetime import datetime, date
from pydantic import BaseModel

class ContactBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    birthday: date
    additional_data: str = None


class ContactResponse(ContactBase):
    id: int = 1
    first_name: str = "Ben"
    last_name: str = "Johnson"
    email: str = "example@test.com"
    phone_number: str = "1234567890"
    birthday: date = date(year=1977, month=7, day=7)
    additional_data: str = "Created first contact for test"

    class Config:
        orm_mode = True