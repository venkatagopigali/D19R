# def croom1(a,b,c):
#     print("a===",a)
#     print("b===",b)
#     print("c===",c)
#     print(a+b+c)
# croom1([10,20,30],[87423,28,2389])


# def croom1(a=50,b=30,c=30):
#     print("a===",a)
#     print("b===",b)
#     print("c===",c)
#     print(a+b+c)
# croom1()

# def croom1(a,b,c):
#     print("a===",a)
#     print("b===",b)
#     print("c===",c)
#     print(a+b+c)
# croom1(10,c=20,b=10)

# def total(*a):
#     print(a)
#     s=0
#     for i in a:
#         s=s+i
#     print(s)
# total(10,2,3,4,5,6,7,8,9,0)


def details(**a):
    k=[]
    v=[]
    d={}
    for i in a:
        k.append(i)
    for i in a.values():
        v.append(i)
    for i in range(len(k)):
        d[v[i]]=k[i]
    print(d)
details(name='dinesh',age=22,phone=1234567890,email='dinesh@gmail.com')