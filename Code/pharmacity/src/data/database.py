from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:nam1ahai@localhost/dbo.drugtest"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = (
    declarative_base()
)  # khai báo "kiến trúc" để so sánh với cơ sở dữ liệu. Có thể hiểu là cơ sở dữ liệu mô phỏng so sánh với bản gốc
