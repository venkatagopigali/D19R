# l=[1,4,7,18,77,45,16,93,69,63,33,30]
# l1=[]
# # print(len(l))
# for i in range(-1,-(len(l)+1),-1):
#     # l1.append(l[i])
#     l1=l1+[l[i]]
# print(l1)


# l=[1,4,7,18,77,45,16,93,69,63,33,30]
# l1=[]
# for i in l:
#     l1=[i]+l1
# print(l1)


# l=[1,4,7,18,77,45,16,93,69,63,33]
# a=len(l)-1
# for i in range(len(l)//2):
#     l[i],l[a]=l[a],l[i]
#     a=a-1
# print(l)

# l=[1,2,3,4,5,5,2,34,'fywevf']
# a=0
# for i in range(len(l)):
#     b=l[i]
#     l.pop(i)
#     l=[b]+l
# print(l)


# l=[1,2,'harika','sravya','kalyan','dinesh']
# l1=[]
# l2=[]
# n=4
# for i in range(len(l)-n,len(l)):
#     l1=l1+[l[i]]
# for i in range(len(l)-n):
#     l2=l2+[l[i]]
# l3=l1+l2
# print(l3)


# a=[27,10,50,100,20,0,25]
# n=3
# for i in range(n):
#     b=a[-1]
#     a.pop(-1)
#     a=[b]+a
# print(a)
