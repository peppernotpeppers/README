from fastapi import Depends, FastAPI, status, HTTPException
from sqlalchemy import false
from sqlalchemy.orm import Session

from data import models, schemas
from data.database import engine, SessionLocal
from data.models import Medicine, Guest, Staff


models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# Dependency
def create_database():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Khởi tạo các phương thức Đọc, Tạo, Sửa, Xóa của thuốc
# Tạo thuốc bằng ID
@app.post("/medicine", status_code=status.HTTP_201_CREATED)
def create_medicine(
    medicine: schemas.Medicine, session: Session = Depends(create_database)
):
    db_createMEC = models.Medicine.create(medicine)
    session.add(db_createMEC)
    session.commit()
    session.refresh(db_createMEC)
    return db_createMEC


@app.get("/medicine/{id}")
def read_medicine(id_drug: int):
    session = Session(bind=engine, expire_on_commit=False)
    readMec = session.query(models.Medicine).get(id_drug)
    session.close()
    return readMec


@app.put("/medicine/{id}")
def update_medicine(id_drug: int, drug_name: str):
    session = Session(bind=engine, expire_on_commit=False)
    readMec = session.query(models.Medicine).get(id_drug)
    if readMec:
        readMec.drug_name = drug_name
        session.commit()
    session.close()
    return readMec


@app.delete("/medicine/{id}")
def delete_medicine(id_drug: int):
    session = Session(bind=engine, expire_on_commit=False)
    readMec = session.query(models.Medicine).get(id_drug)

    if readMec:
        session.delete(readMec)
        session.commit()
        session.close()

    else:
        raise HTTPException(
            status_code=404, detail=f"todo item with id {id_drug} not found"
        )

    return f"Đã xóa thành công ID {id_drug}"


@app.get("/medicine")
def read_all_medicine(cm: schemas.Medicine):
    return "Đọc tất cả dữ liệu trong bảng thuốc"
