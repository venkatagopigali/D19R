# class mobile:
#     def lock(self):
#         print("no password")
#     def camera(self):
#         print("50px")
#     def battery(self):
#         print("2%")
# class snapchat(mobile):
#     def camera(self):
#         a=input("you want real pic or filter")
#         if a=='real':
#             super().camera()
#         else:
#             print("filter --------")
#             super().camera()
# class instagram(mobile):
#     def reels(self):
#         print("coode for reels")
#     def camera(self):
#         print("40px")
# s=snapchat()
# s.camera()
# i=instagram()
# i.camera()

# class nokia:
#     def __init__(self):
#         print("screen password")
#     def applock(self):
#         print("app lock")

# class whatsapp(nokia):
#     def __init__(self):
#         super().applock()
#         print("chatting")
# class instagram(nokia):
#     def __init__(self):
#         p=int(input("enter your password"))
#         if p==1234:
#             super().applock()
#             print("chatting-------")
# # i=instagram()
# print(instagram.mro())