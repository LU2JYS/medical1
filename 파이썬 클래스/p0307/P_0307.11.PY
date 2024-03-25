list=[1,2,3]
alist=[*list] #동기화가 된것이다. #1 깊은복사이다.
alist=list[:] #2


list[0]=100
print(alist)

a=100
b=a
a=10
print(b)
