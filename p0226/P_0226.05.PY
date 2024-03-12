#얕은 복사 깊은 복사
#변수
'''
a=1
b=2
c=a
print(a,b,c)
a=8
print(a,b,c,)

a=8
print("변수:", a,b,c)

print(id(a))
print(id(b))
print(id(c))
'''
#변수의 값이 변하는 변수는 다은 메모라 주로로 옮긴다.
# 기존과 메모리 값이 바뀌에 됨을 확인 할수있다.

# 리스트의 경우 
#리스트 여러가지 데이터가 들어갈수있다.
# 주소값이 할당이 된다.
#단순복사는 주소값이 복사가 된다.
'''
aa=[1]
bb=[2]
cc=aa
print(aa,bb,cc)
print(id(bb))
print(id(cc))
aa[0]=10
print(aa,bb,cc)
print(id(bb))
print(id(cc))
#단순복사가 되었기때문에 aa의 값을 변경하려면 cc값이 같이 반역
'''

'''
#깊은복사>>>>>>>>>>>중요하다
#독립성
aa=[1]
bb=[2]
cc = copy.deepcopy(aa)
print(aa,bb,cc)
print(id(aa))
print(id(bb))
print(id(cc))
aa[0]=10
print(aa,bb,cc)
print(id(aa))
print(id(bb))
print(id(cc))
'''