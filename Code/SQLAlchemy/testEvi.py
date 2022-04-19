from sqlalchemy import create_engine, text


#thiết lập kết nối tới database theo format :
#  "postgresql://(user - mặc định là posgres):(password)@localhost:(port - mặc định là 5432)/ (tên db) "
engine = create_engine("postgresql://postgres:nam1ahai@localhost:5432/dbo.drugtest", echo=True, future=True)
print('connect success')

with engine.connect() as conn:
    resu = conn.execute(text("SELECT * FROM  tbl_drug"))
    print(resu.all())
