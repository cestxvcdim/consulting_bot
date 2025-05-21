from db_logic.database import SessionLocal
from db_logic.models import User


def create_user(**kwargs) -> User | None:
    db = SessionLocal()
    try:
        db_user = User(**kwargs)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    finally:
        db.close()


def get_user_by_tg_id(user_id: int) -> User | None:
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.chat_id == user_id).first()
        return user
    finally:
        db.close()
