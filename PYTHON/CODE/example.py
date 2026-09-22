import pymysql
import pandas as pd
conn=pymysql.connect(
    host="localhost",
    port=3306,
    user='root',
    password='gopi@1234',
    database="d19r"
)
# cur=conn.cursor()
# cur.execute("select * from orders_2024_jan_jun")
# for i in cur:
#     print(i)
data=pd.read_sql("select * from orders_2024_jan_jun",conn)
print(data.to_string())