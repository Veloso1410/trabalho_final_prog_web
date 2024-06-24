# IMPORT 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# DATABASE URL
DATABASE_URL = "postgresql://postgres:1410@localhost:5432/armas"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
