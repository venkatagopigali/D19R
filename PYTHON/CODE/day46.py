import pymysql
conn=pymysql.connect(
    host='localhost',
    user='root',
    port=3306,
    password='gopi@1234',
    database='d19r'
)
cur=conn.cursor()
# cur.execute("desc emp")
# for i in cur:
#     print(i)
# while True:
#     try:
#         print("1.insert\n2.update\n3.delete\n4.display")
#         op=int(input("ENter your option    :"))
#         if op==1:
#             print("insert opration")
#             empid=int(input("Enter EMPID        :"))
#             name = input("Enter Emp Name     :")
#             dept = input("Entre Emp departmnet    :")
#             salary=int(input("Entre Emp salary    :"))
#             age =int(input("Enter emp age      :"))
#             city=input("Enter Emp City       :")
#             cur.execute("insert into emp values(%s,%s,%s,%s,%s,%s)",(empid,name,dept,salary,age,city))
#             conn.commit()
#         elif op==2:
#             print("update operation")
#             empid=int(input("ENter Emp id   :"))
#             salary=int(input("ENter your new salary  :"))
#             cur.execute("update emp set salary=%s where empid=%s",(salary,empid))
#             conn.commit()
#         elif op==3:
#             print("delete operation")
#             empid=int(input("ENter empoid to be deleted  "))
#             cur.execute("delete from emp where empid=%s",(empid))
#             conn.commit()
#         elif op==4:
#             print("show the details")
#             cur.execute("select name,salary from emp")
#             for i in cur:
#                 print(i)
#             conn.commit()
#         else:
#             print("please give valid option")
#     except Exception as e:
#         print(e)

# salary=int(input("Enter your salary   :"))
# cur.execute("select * from a1 inner join a2 on a1.sno=a2.sno")
# for i in cur:
#     print(i)