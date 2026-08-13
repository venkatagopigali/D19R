# l=[]
# print(type(l))
# print(l)

# t=()
# print(type(t))
# print(t)

# s=set()
# print(type(s))
# print(s)

# a=list()
# print(type(a))
# print(a)

# l=[1,2,3,4,5]
# print(l)
# print(type(l))

# l=[5,10,15,0,-9,-50,18,7,45,93,96,99,1,17,77]
# print(l)

# l=['a',1,'b',3.1,'@',True,None,10+2j]
# print(type(l))
# print(l)
# for i in l:
#     print(type(i))


# l=[1,5,10,'goto sleep','trainer',0,38,5.0]
# print(id(l))
# l[3]='wake up'
# print(l)
# print(id(l))

# l=[5,5,5]
# print(l)


# l=[10,20,40,'kowshik','durandhar','raju']
# print(l[1])
# print(l[-7])

# a=[18,1,45,7,9,96,93,33,99,17,333,10,77,3,8]
# print(a[1:11])
# print(a[::])
# print(a[::2])
# print(a[-1::-2])
# print(a[-15::2])
# print(a[::-1])

# a="AyusHMANbhAVA"
# print(a.swapcase())

# print(ord('A'),ord("Z"))
# print(ord('a'),ord('z'))
# a="a"
# print(chr(ord(a)-32))

a="AyusHMANbhAVA"
s=""
for i in a:
    if ord('A')<=ord(i) and ord('Z')>=ord(i):
        s=s+chr(ord(i)+32)
    else:
        s=s+chr(ord(i)-32)
print(s)
