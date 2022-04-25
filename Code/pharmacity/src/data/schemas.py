from datetime import date
from pydantic import BaseModel


# Tạo class Medicine để hỗ trợ cho việc tạo và đọc data
class MedicineBase(BaseModel):
    id_drug: int


class MedicineCreate(MedicineBase):
    pass


class Medicine(MedicineBase):
    drug_code: int
    drug_name: str
    drug_type: str
    drug_quatity: int
    drug_price: int
    drug_date: date
    drug_expire: date
    drug_status: str

    class Config:
        orm_mode = True


# Tạo class Guest để hỗ trợ cho việc tạo và đọc data
class GuestBase(BaseModel):
    guest_email: str


class GuestCreate(GuestBase):
    pass


class Guest(GuestBase):
    id_guest: int
    guest_name: str
    guest_dob: date
    guest_address: str
    type_of_disease: str
    guest_age: date
    guest_phone: int
    guest_sex: str

    class Config:
        orm_mode = True


# Tạo class Staff để hỗ trợ cho việc tạo và đọc data
class StaffBase(BaseModel):
    staff_email = str


class StaffCreate(StaffBase):
    pass


class Staff(StaffBase):
    id_staff = int
    staff_name = str
    staff_dob = date
    staff_address = str
    staff_phone = int
    staff_sex = str

    class Config:
        orm_mode = True
