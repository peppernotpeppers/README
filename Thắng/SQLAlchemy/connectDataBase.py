import psycopg2
from faker import Faker
from FakeFuntionOfDrug import fake, EffectOfDrug, DrugQuatityStatus

# fake = Faker()

conn = psycopg2.connect(database="dbo.drugtest", user="postgres", password="nam1ahai", host="127.0.0.1", port="5432")
print ("Opened database successfully")
cur = conn.cursor()

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

conn.commit()
print ("Records created successfully")
cur.close()
conn.close()