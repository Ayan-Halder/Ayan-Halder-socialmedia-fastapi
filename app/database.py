from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"
SQLALCHEMY_DATABASE_URL = "postgres://xuzijnpwwcitps:528ec2568f6f03e2fa045a200444dfc08baf5c0e684c7903e2a8781b5eaa3fe0@ec2-44-195-162-77.compute-1.amazonaws.com:5432/damdbbavd5euig"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


while True:
    try:
        conn = psycopg2.connect(host='localhost', database ='fastapi', user='postgres',
        password='Ayan1999$', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Detabase connected successfully")
        break
    except Exception as error:
        print("Error connecting to database")
        print("Error: ", error)
        time.sleep(2)