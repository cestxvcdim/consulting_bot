from zoneinfo import ZoneInfo

from sqlalchemy import Column, Integer, String, DateTime, BigInteger
from datetime import datetime

from db_logic.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    chat_id = Column(BigInteger, unique=True, nullable=False)
    registered_at = Column(DateTime, default=datetime.now(ZoneInfo("Europe/Moscow")))

    full_name = Column(String(105), nullable=True)
    phone_number = Column(String(12), nullable=True)
    email = Column(String(70), nullable=True)

    def __str__(self):
        return f"{self.id}: {self.chat_id}"
