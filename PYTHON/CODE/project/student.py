import pymysql
conn=pymysql.connect(
    host='localhost',
    user='root',
    port=3306,
    password='gopi@1234',
    database='d19r'
)
cur=conn.cursor()
class student:
    def job_app(self):
        print("1.register\n2.login")
        op=input("Choose your option    :")
        if op=='1':
            print("plase register here")
            email = input("ENter your email    ")
            name  = input("ENter your name   ")
            password= input("ENter your password    ")
            skills = input("ENter your skills    ")
            qualification = input("ENter your qua    ")
            mobile = int(input("ENter your mobile    "))
            experince = int(input("ENter your exp    "))
            cur.execute("insert into job_app values(%s,%s,%s,%s,%s,%s,%s)",(email,name,password,skills,qualification,mobile,experince))
            print("ypur register successfully------")
            conn.commit()
        elif op=='2':
            print("please login here ---------------------")
            email=input("ENter your email    ")
            password= input("ENter your password    ")
            cur.execute("select * from job_app")
            for i in cur:
                if email==i[0] and password==i[2]:
                    print("login successfully")
                    print("1.view profile\n2.update\n3.withdraw")
                    op=input("Enter your option    :")
                    if op=='1':
                        cur.execute("select * from job_app where email=%s",(email))
                        for i in cur:
                            print("Email      :",i[0])
                            print("name       :",i[1])
                            print("password   :",i[2])
                            print("skills     :",i[3])
                            print("qua        :",i[4])
                            print("mobile     :",i[5])
                            print("exp        :",i[6])
                    elif op=='2':
                        skills=input("Enter your new skillss   :")
                        password=input("Enter your new password    :")
                        cur.execute("update job_app set skills=%s,password=%s where email=%s",(skills,password,email))
                        print("updates successfuly")
                        conn.commit()
                    elif op=='3':
                        cur.execute("delete from job_app where email=%s",(email))
                        conn.commit()
                    else:
                        print("please give valid option")
                else:
                    continue
        else:
            print("Valid option")