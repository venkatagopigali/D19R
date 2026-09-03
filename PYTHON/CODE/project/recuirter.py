import pymysql
conn=pymysql.connect(
    host='localhost',
    user='root',
    port=3306,
    password='gopi@1234',
    database='d19r'
)
cur=conn.cursor()
class recuirter:
    def rec_login(self):
        while True:
            email=input("Enter your email     :")
            password=input("Entre your password    :")
            cur.execute("select * from recuirter")
            for i in cur:
                if email==i[2] and password==i[3]:
                    print("login success fully")
                    cur.execute("select * from job_app")
                    for i in cur:
                        print(i)
                    break
                else:
                    continue
            break
            # else:
            #     print("please give valid email or password")
        
