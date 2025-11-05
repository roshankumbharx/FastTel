from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import create_engine
from config import settings


engine = create_engine(settings.db_url)
session  = sessionmaker(autoflush=False,autocommit=False,bind = engine)