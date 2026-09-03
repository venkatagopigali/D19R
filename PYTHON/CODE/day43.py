# try:
#     a=int(input("Enter data     :"))
#     b=int(input("Enter data     :"))
#     print(a/b)
# except ValueError:
#     print("give data properly ")
# except ZeroDivisionError:
#     print("donnot metion 0 as denominator")


# import pandas as pd
# try:
#     data=pd.read_csv(r"C:\Users\hp\Desktop\BOOTCAMP\heart_disease_messy.csv")
#     print(data.to_string())
# except FileNotFoundError:
#     print("please check the file location or file name")

# try:
#     a=[10,20,40,60,70,80,90]
#     print(a[10])
# except IndexError:
#     print("plase check the index position")

# try:
#     d={"name":'dinesh','age':21,'year':2026}
#     # print(d.get('phone'))
#     print(d['phone'])
# except KeyError:
#     print("please check keys in dict")
# try:
#     a=int(input("Enter index pos1 :"))
#     b=int(input("Enter index pos2 :"))
#     print(a/b)
#     l=[10,20,40]
#     print(l[a])
#     d={"name":'dinesh','age':21,'year':2026}
#     # print(d.get('phone'))
#     print(d['age'])
# except ZeroDivisionError:
#     print("donot give zero in denominator")
# except ValueError:
#     print("please check datarypes")
# except IndexError:
#     print("please check the index")
# except KeyError:
#     print("please ckeck keys")


# try:
#     # print(gopi)
#     a=float(input("Enter index pos1 :"))
#     b=int(input("Enter index pos2 :"))
#     print(a/b)
#     l=[10,20,40]
#     print(l[a])
#     d={"name":'dinesh','age':21,'year':2026}
#     # print(d.get('phone'))
#     print(d['age'])
# except Exception as e:
#     print(e)

# a=int(input("enter num "))
# print(a)
# a=3/2
# print(a)