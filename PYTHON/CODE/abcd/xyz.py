def f1(a):
    if (a%400==0 or a%4==0) and (a%100)!=0:
        print("leap year")
    else:
        print("not leap year")