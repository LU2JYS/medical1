a=10
b=a #변수 복사
b=100
print(a)
print(b)

print("-"*40)
a_list=[1,2,3]
b_list=a_list #리스트를 복사 이렇게 주소값을 복사하여 하면안됨(얕은복사)>>깊은복사해야함
b_list[0]=200
print(a_list[0]) #200
print(b_list[0]) #200