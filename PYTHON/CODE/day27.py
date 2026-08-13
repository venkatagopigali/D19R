# def _10000Coders(name):
#     print(f"Hello {name}")
#     print("congratulation.. you are successfulyy getting job")
#     print("with regard\n10000Coders")
# _10000Coders("VIJAY DEVARAKONDA")
# _10000Coders("varshith")


# def hello():
#     print("Good Morning")
#     print("ayushman bhava")
#     a=int(input())
#     b=int(input())
#     print(a+b)
# hello()

# def certificate(name,year,per,branch):
#     print("                 CERTIFICATE      ")
#     print("======================================")
#     print("name          :",name)
#     print("graduation    :",year)
#     print("percentage    :",per)
#     print("branch        :",branch)
#     print("                                         ")

# certificate("BOB",2026,100,'CINEMA')
# certificate("Namratha",2024,98,'CIMENA')


def max_element(a):
    l=[]
    for i in a:
        if i.isdigit():
            l=l+[int(i)]
    print(l)
    max=l[0]
    for i in l:
        if max<i:
            max=i
    print(max)
max_element("venkatagopigali10000coders@gmail.com")
max_element("venkatagopigali6@gmail.com")
max_element('ayushmanbhava287342@gmail.com')