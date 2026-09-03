# print("Hello")

# if 10:
#     print("ok")
# else:
#     print("not ok")

# a=10
# b=20
# print(a+b)
# c=10%0
# print(c)


# a=int(input("enter your number :"))
# b=int(input("enter your second number :"))
# try:
#     c=a%b
#     print(c)
# except ZeroDivisionError:
#     print("donnot give zero as divisor")

# A="Kowshik"
# try:
#     print(A)
# except NameError:
#     print("please declare variable properly")

try:
    a=int(input("enter data :"))
    print(a)
except ValueError:
    print("please check datatypes")