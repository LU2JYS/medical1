# 변수

a= False
b= 123
c= 1.23456
d= "문자"
e=[1,2,3]
'''
#출력
print("안녕하세요")
print("123+3451")
str1="반갑습니다."
print(str1)
print("{:S} : {1:d} / {2:d} : {3:f}".format("수식",7,3,7/3))
print("{} : {} = {} ".format("수식",7,3,7/3))
'''
#관계연산자
# > : 크다 >= : 크거나 같다
# < : 작다 >= : 작거나 같다
# == :같다 != : 같지 않다
print(3>5) #결과가 거짓
n1=10
n2=8
print(n1!= n2)
print( 3<n1<100)

#if n1<10

#논리연산자 :and or not
a,b=10,9
print("and연산자") #둘다 참이어야 참이다
if a ==10 and b==9:
    print("참 and 거짓 =참")
else :
    print("참 and 참 =참") 
    
if a == 10 and b != 9 :
    print("참 and 거짓 =참")
else :
    print("참 and 거짓 =거짓")
if a != 10 and b == 9 :
    print("참 and 거짓 =거짓")
else :
    print("참 and 거짓 =거짓")
if a != 10 and b != 9 :
    print("참 and 거짓 =참")
else :
    print("참 and 거짓 =거짓")           
    
print("or연산자")
if a ==10 or b==9:
    print("참 or 거짓 =참")
else :
    print("참 or 참 =참") 
    
if a == 10 or b != 9 :
    print("참 or 거짓 =참")
else :
    print("참 or 거짓 =거짓")
if a != 10 or b == 9 :
    print("참 or 거짓 =거짓")
else :
    print("참 or 거짓 =거짓")
if a != 10 or b != 9 :
    print("참 or 거짓 =참")
else :
    print("참 or 거짓 =거짓")   

print("not연산자") #> 참은 거짓으로 / 거짓은 참으로 변경해준다
if not a==10:
    print("not 참 =참")
else:
    print('not 참 =거짓')
if not a!=10:
    print("not 거짓 =참")
else:
    print('not 거짓 =거짓') 

#조건문 if
#if 조건문 1:
#    실행문 1   
#elif 조건문 2:
#    실행문 2
#else:
#     실행문3
#조건문이 1이 참이면 실행문1을 실행 후 종료
#elif 가 있으면 
#즉 조건문1이 거짓이고 조건문2가 참이면 실행문2 실행 후 종료
#조건문1,2,가 거짓이면 실행문 실행후 종료
'''
num = 5
#숫자가 0이상이면 양수를 출력하시요
if num >0:
    print("양수입니다")
#숫자가 0이상이면 양수를 출력하고 음수면 음수를 축력하시요
if num >=0:
    print("양수입니다")
else:
    print("음수입니다")
if num>0:
    ("양수입니다") 
elif num==0:
    ("0입니다")  
else:
    print("음수입니다.")     
    
#실행문을 비우고 싶을때 :pass
if 1==1:
    pass  
else:
    print("else문 실행")
'''    
'''
#중첩 if문 : if문 안에 if 문 사용
if num >=0:
   if num ==0:
   print("0입니다")
else:
    print("양수입니다")
    '''