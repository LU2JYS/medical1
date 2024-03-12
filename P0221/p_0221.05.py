#변수
# int형
# 10진법: 정수 1,2,3,.........-1,-2,-3 >>>>>>주로 이거를 많이 쓴다...
num1 =10
print(num1)
print(10)
num2=20
print(num2)

# 2진법 : 0b로 시작한다
num3=0b101010 #1* 2^5 + 0* 2^4 + 1*2^3 + 0*2^2+1*2^1+ 0*2^0
# 32+8+2 = 42
print(num3)


# 8진법 : 0o로 시작한다
num4 = 0o52
print(num4)
# 5*8^1 + 2*8^0
# 40+2=42

#16진법 : 0x로 시작한다. 1,2,3,4,5,6,7,8,9,a,b,c,d,e,f,g, 의 수로 표현
num5= 0x2a
print(num5)
# 2*16+10 = 32+10 =42

print("----------------------------")

#float 형 : 실수 즉 소수점을 포함하고 있는 수>>>>>>>>>>>>>>>>>주로 이거를 많이 쓴다...
num6 = 3.14
print("%f"%num6)
num7 = 2*3.14*5
print(num7)

print("----------------------------")

#complex 형 : 실수 +허수
#3+2i 파이썬에서는 i대신 j를 사용한다.
comp1 =3+4j
print(comp1)
print(comp1.real)
print(comp1.imag)


print("----------------------------")

#boolean 참 거짓 판별
bool1= True
bool2= False
print("bool1 : ",bool1)
print("bool2 : ",bool2)
bool3 = (1==2) #false
print("bool3 : ",bool3)


print("----------------------------")
# string형 
str1 ="안녕하세요"
str2 ="hello"
print(str1)
print(str2)