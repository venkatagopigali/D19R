import pymysql
conn=pymysql.connect(
    host='localhost',
    port=3306,
    user="root",
    password='gopi@1234',
    database='d19r'
)
cur=conn.cursor()
# cur.execute("select * from emp")
# for i in cur.fetchall():
#     print(i)
# conn.commit()

empid=int(input("Enter EMPID        :"))
name = input("Enter Emp Name     :")
dept = input("Entre Emp departmnet    :")
salary=int(input("Entre Emp salary    :"))
age =int(input("Enter emp age      :"))
city=input("Enter Emp City       :")

cur.execute("insert into emp values(%s,%s,%s,%s,%s,%s)",(empid,name,dept,salary,age,city))

conn.commit()