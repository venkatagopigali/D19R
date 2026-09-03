# class meta:
#     def chat(self):
#         print("code for chat")
#     def call(self):
#         print("code for call")
#     def stories(self):
#         print("code for stories")
# class whatsapp:
#     def stories(self):
#         print("code for whatsapp stories")
#     def payment(self):
#         print("code for payment")
# class insta(whatsapp,meta):
#     def reels(self):
#         print("code for reels")
#     def chat(self):
#         print("new chat code for insta")

# i=insta()
# i.reels()
# i.chat()
# i.call()
# i.stories()
# w=whatsapp()
# w.payment()
# # w.call()
# # w.chat()
# print(insta.mro())

# print(10+20)
# print((10).__add__(20))
# print(10>20)
# print((10).__gt__(20))

class dunder:
    def __init__(self,a):
        self.a=a
    def __add__(self,other):
        return self.a-other.a
    def __sub__(self,other):
        return self.a+other.a
    def __lt__(self,other):
        return self.a>=other.a
    def __mul__(self, other):
        return self.a//other.a

d=dunder(20)
d1=dunder(30)
print(d+d1)
print(d-d1)
print(d>d1)
print(d*d1)

