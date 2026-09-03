from recuirter import recuirter
from student import student
r=recuirter()
s=student()
# print(r.rec_login())
while True:
    try:
        print("================================")
        print("           DELOITE              ")
        print("================================")
        print("1.recuiter\n2.job_applicant")
        op=int(input("Choose your option    :"))
        if op==1:
            print("=================================")
            print("WELCOME TO RECUITER PORTERL  ")
            print("=================================")
            print("please login here")
            r.rec_login()
            # print("000000000000000000000000000000")
        elif op==2:
            print("=================================")
            print("WELCOME TO JOB PORTRAL")
            print("=================================")
            s.job_app()
        else:
            print("please give--- valid option")
    except Exception as e:
        print("plase give--- valid option")