from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from backend.config.settings import settings

# Create database engine
engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)


# Create database session factory
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


# FastAPI database dependency
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# Test database connection
def check_database_connection():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
        return True
