from sqlalchemy import BigInteger, Column, String, Integer, Date

# from sqlalchemy.orm import relationship
from data.database import Base


class Medicine(Base):
    __tablename__ = "tbl_drug"

    id_drug = Column(Integer, primary_key=True, index=True)
    drug_code = Column(BigInteger, unique=True, index=True)
    drug_name = Column(String)
    drug_type = Column(String)
    drug_quatity = Column(Integer)
    drug_price = Column(BigInteger)
    drug_date = Column(Date)
    drug_expire = Column(Date)
    drug_status = Column(String, index=True)

    @classmethod
    def create(cls, obj: any):
        instance = cls()
        for k in dict(obj):
            setattr(instance, k, getattr(obj, k, ""))
        return instance


class Guest(Base):
    __tablename__ = "tbl_guest"

    id_guest = Column(Integer, primary_key=True, index=True)
    guest_name = Column(String, unique=True, index=True)
    guest_dob = Column(Date)
    guest_address = Column(String)
    guest_email = Column(String)
    type_of_disease = Column(String)
    guest_age = Column(Date)
    guest_phone = Column(BigInteger)
    guest_sex = Column(String, index=True)


class Staff(Base):
    __tablename__ = "tbl_staff"

    id_staff = Column(Integer, primary_key=True, index=True)
    staff_name = Column(String, unique=True, index=True)
    staff_dob = Column(Date)
    staff_address = Column(String)
    staff_email = Column(String)
    staff_phone = Column(BigInteger)
    staff_sex = Column(String)
