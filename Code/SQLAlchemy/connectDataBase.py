import psycopg2
from FakeFuntionOfDrug import fake, EffectOfDrug, DrugQuatityStatus, RandomGender

# fake = Faker()

conn = psycopg2.connect(database="dbo.drugtest", user="postgres", password="nam1ahai", host="127.0.0.1", port="5432")
print ("Opened database successfully")
cur = conn.cursor()

# Tạo vòng lặp 'for' để ném data vào bảng tbl_drug
for i in range (1,34):
    id_drug = i                                 #Tạo id theo số thứ tự và auto-increment
    drug_code = fake.msisdn()                   #số điện thoại fake, được gán làm mã thuốc
    drug_name = fake.name()                     #Tên giả
    drug_type = EffectOfDrug.effectName()                   #Fake tác dụng của thuốc
    drug_quatity =fake.random_number()
    drug_price = fake.random_int(min=0, max=9999)
    drug_date = fake.date_time()
    drug_expire = fake.date_time()
    drug_status = DrugQuatityStatus.quatityStatus()
    cur.execute("INSERT INTO tbl_drug (id_drug, drug_code, drug_name, drug_type, drug_quatity, drug_price, drug_date, drug_expire, drug_status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (id_drug, drug_code, drug_name, drug_type, drug_quatity, drug_price, drug_date, drug_expire, drug_status))

#Tạo vòng lặp for để ném data vào bảng tbl_guest
for i in range (1,34):
    id_guest = i
    guest_name = fake.name()
    guest_dob = fake.date()
    guest_address = fake.street_address()
    guest_email = fake.email()
    type_of_disease = EffectOfDrug.effectName()
    guest_age = fake.random_int(min=0, max = 70)
    guest_phone = fake.phone_number()
    guest_sex = RandomGender.gender()
    cur.execute("INSERT INTO tbl_guest (id_guest, guest_name, guest_dob, guest_address, guest_email, type_of_disease, guest_age, guest_phone, guest_sex) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (id_guest, guest_name, guest_dob, guest_address, guest_email, type_of_disease, guest_age, guest_phone, guest_sex))

#Tạo vòng lặp for để ném data vào bảng tbl_guest
for i in range (1,34):
    id_staff = i
    staff_name = fake.name()
    staff_dob = fake.date()
    staff_address = fake.street_address()
    staff_email = fake.email()
    staff_phone = fake.random_int(min=0, max = 70)
    staff_sex = RandomGender.gender()
    cur.execute("INSERT INTO tbl_staff (id_staff, staff_name, staff_dob, staff_address, staff_email, staff_phone, staff_sex) VALUES (%s, %s, %s, %s, %s, %s, %s)", (id_staff, staff_name, staff_dob, staff_address, staff_email, staff_phone, staff_sex))


conn.commit()
print ("Records created successfully")
cur.close()
conn.close()