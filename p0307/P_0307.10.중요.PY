
#공간을 만들어 놓고 for문을 만드는 방법
list=[0]*10
for i in range(10):
    list[i]=i+1
print(list)

#컴프리헨션을 사용하는 방법>>>>>>>>>>>중요
list1=[i+1 for i in range(10)]
print(list1)


#컴프리헨션으로 미리 방을 만들고 넣는게 편하다...
#이차원리스트이다 : 크기가 지정이 안됨.

a_list=[]
a_list.append(0)
a_list.append(1)
a_list.append(2)
a_list[0]=3
print(a_list)