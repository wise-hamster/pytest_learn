from pydantic import BaseModel, field_validator
from src.enums.user_enums import Genders, Statuses
from email_validator import validate_email, EmailNotValidError
from src.enums.global_enums import GlobalErrorMessages


class User(BaseModel):
    id: int
    name:str
    email: str
    gender: Genders
    status : Statuses

    @field_validator('email')
    def validate_email_simple(cls, email):
        if '@' not in email or '.' not in email.split('@')[-1]:
            raise ValueError(GlobalErrorMessages.WRONG_EMAIL_NO_VALID.value)
        return email

class UserList(BaseModel):
    meta:dict
    data:list[User]