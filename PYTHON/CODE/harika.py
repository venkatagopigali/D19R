def function(l):
    c=0
    for i in l:
        c=c+1
    print(c)

def n_s_c(l):
    n=0
    s=0
    for i in l:
        if type(i)==int or type(i)==float:
            n=n+1
        else:
            s=s+1
    print("numbers count ",n)
    print("string count  ",s)

class A:
    def dinesh(self,a):
        l=len(a)-1
        for i in range(0,len(a)//2):
            a[i],a[l]=a[l],a[i]
            # print(i,l)
            l=l-1
        print(a)


