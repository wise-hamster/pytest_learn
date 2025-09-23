from pydantic import BaseModel #BaseModel - для создания модели
from pydantic import IPvAnyAddress #IPvAnyAddress - валидация по IP
from pydantic import HttpUrl  #Проверяет URL
from pydantic import UUID4 # Проверка соответствия UUID тому, что заложено
from pydantic import EmailStr #Проверка email
from pydantic import model_validator
from src.enums.user_enums import Statuses
from pydantic.types import PastDate, FutureDate #для валидации дат по времени
from typing import List
from pydantic_extra_types.payment import PaymentCardNumber
from pydantic_extra_types.color import Color

class Physical (BaseModel):
    color: Color
    photo:HttpUrl
    uuid: UUID4

class Owners (BaseModel):
    name: str
    card_number: PaymentCardNumber
    email: EmailStr

class DetailedInfo(BaseModel):
    physical: Physical
    owners: List [Owners]

class Computer(BaseModel):
    status : Statuses
    activated_at: PastDate
    expiration_at: FutureDate
    host_v4: IPvAnyAddress
    host_v6: IPvAnyAddress
    detailed_info: DetailedInfo


comp = {
  "status": "active",
  "activated_at": "2023-01-01",
  "expiration_at": "2025-12-31",
  "host_v4": "192.168.1.1",
  "host_v6": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
  "detailed_info": {
    "physical": {
      "color": "red",
      "photo": "https://example.com/photo.jpg",
      "uuid": "550e8400-e29b-41d4-a716-446655440000"
    },
    "owners": [
      {
        "name": "John Doe",
        "card_number": "4000000000000002",
        "email": "john.doe@example.com"
      },
      {
        "name": "Jane Smith",
        "card_number": "5555555555554444",
        "email": "jane.smith@example.com"
      }
    ]
  }
}


