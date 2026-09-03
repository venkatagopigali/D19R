# class pavan:
#     n="D19R"          #public varible
#     _a=60             #protected
#     def name(self):
#         print("inside class m1 :",pavan.n)
#         print("inside class m1 :",pavan._a)
#     def age(self):
#         print("inside class m1 :",pavan.n)
#         print("inside class m2 :",pavan._a)
# class kalyan:
#     def name1(self):
#         print("outside class m1 :",pavan.n)
#         print("outside class m1 :",pavan._a)
#     def age1(self):
#         print("outside class m2 :",pavan.n)
# # p=pavan()
# # p.name()
# # p.age()


# k=kalyan()
# k.name1()
# # print("out side classes ",pavan.n)


# class A:
#     __a="Ayushmanbhava"
#     def __name(self):
#         # self.__a=a
#         print("same methods   ",A.__a)
#     def name1(self):
#         print("anthor methods   ",A.__a)

# class B(A):
#     def age1(self):
#         print("in anthor clS  ",A._A__a)


# # a=A()
# # a.name()
# # a.name1()
# b=B()
# b._A__name()
# b.age1()

# from abc import ABC,abstractmethod

# class Bank(ABC):
#     @abstractmethod
#     def withdraw(self):
#         a=1000
#         b=int(input("enter your amount :"))
#         if a<b:
#             print("check your bank balence")
#         else:
#             print("withdraw")
# class ATM(Bank):
#     def withdraw(self):
#         super().withdraw()
# # b=Bank()
# # b.withdraw()
# a=ATM()
# a.withdraw()

