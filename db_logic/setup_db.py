"""File contains the init_db function."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from config import Config

from model import Base

engine = create_engine(Config.db_path, connect_args={'check_same_thread': False}, poolclass=StaticPool)
DBSession = sessionmaker(bind=engine)

def init_db():
    """Initialize the database with requirement fields."""
    Base.metadata.create_all(engine)
