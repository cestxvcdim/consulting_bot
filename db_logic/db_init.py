from db_logic.database import engine, Base
from db_logic.models import User

if __name__ == "__main__":
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        print(e)
