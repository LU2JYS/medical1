#변수
#기본: bool,int,float,string>>>>>>>>>>>>중요
#list, tuple, dict
'''
a=True
b=False
print("bool형은 {},{}가 있다".format(a,b))

c=45
print("int형은 정수 {:d}와 같은 숫자".format(c))
print("%d"%(c))

d=3.1234567489
print("float형은 정수 {:.2f}와 같은 소숫점이 있는 숫자".format(d))

e="문자" #string type
print("문자열입니다.")
print(e+"입니다")
print(e,"입니다")
print("{:s}입니다".format(e))
'''
'''
#input() -콘솔창에서 입력을 받는다.
print("글자를 콘솔창에 보여준다.")
str1=input("입력하세요>>")
print("{}은 입력한 방법입니다.".format(str1))

n1= input("첫번째 숫자를 입력하세요>>>")#10
n2=int(input("두번째 숫자를 입력하세요"))#3
#n1*n2 값을 출력해보세요
#숫자로 출력해보세요
print(int(n1)*n2)
'''

#조건문

#if 조건문1:
#     실행문1
#elif  조건문2:
#       실행문2
#else:
#        실행문3    
#조건문이1이 참이면 실행문이1 실행
#조건문1이 거짓이고 조건문2가 참이면 실행문 2실행
#조건문1,조건문2 거짓이면 실행문3 실행
# elif,else, 생략가능하다

#if 실행문을 비우고 싶을때 :pass
#if 조건문:
#    pass
'''
a=3
if a ==0:
    print("if문 실행")
    print("들여쓰기 중요")
    print("들여쓰기된 전체 실행")
elif a==1:
    print("첫번째로elif문 실행")
elif a==2:
    print("드번째로elif문 실행")
elif a==3:
    print("세번째로elif문 실행")
else:
    print("else문 실행")
'''    
#if 문 중첩
#0보다 크면 양수 작으면 음수를 출력하고
#10보다 작으면 [10보다 작으면] 크면 [10보다 큼] 을 출력
'''
n=9
if n >=0:
    print("양수")
    if n >=10:
        print('10보다 큼')
    else:
        print("10보다 작음")
else:
    print("음수")
    
if n>=0 and n<=10:
    print("양수")
    print("10보다 작음")
elif n>=0 and n<=10:
    print("양수")
    print("10보다 작음")
else:
    print("음수")
'''    
''' 
n=int(input("숫자를 입력하세요>>>"))
if n % 2==0:
    print("짝수입니다")
else:
    print("홀수입니다")
'''     

'''   
num=int(input("학생의 점수를 입력하시요"))
if num>=90:
    print("A학점입니다")
    if num>=98:
        print("A+입니다")
    elif num>=93:
        print("A입니다")
    else:
        print("A-입니다")
elif num>=80:
    print("B입니다")
    if num>=88:
        print("B+입니다")
    elif num>=83:
        print("B입니다")
    else:
        print("B-입니다")
else:
    print("이하는 F학점")
'''  
''' 
# list
# 리스트변수명을 요소 하나하나 지정된 값이 있다.
#리스트변수명을 (int,bool,float,stirng,list)
l1=["홍길동",100]
l2=[[2,3,5,],[4,5,6]]
l3=[True,[4,5,6],"hello",[1,2],3.14,5,]
#파이썬은 대소문자를 구별한다.
# 참 거짓도 앞에 대문자를 구별한다.
print(l1[0])
print(l2[1][1])
print(l3[1])
print(l3[3])
print(l3[4][0])
print(l3[6])
'''
'''
#인덱싱을 가지고 리스트의 특정 요소를 값을 수정할수있다.
l1=["홍길동",100]
l1[1]=90
print(l1)
l1[0]="이순신"
print(l1)
'''
'''
l3[0]=False
l3[2]=3.14
l3[3]="hi"
l3[5][1]=2
'''
'''
num=[0,1,2,3,4,5,6,7,8,9,10]
print(num[1:6])

str1=["a","b","c","d","e","f"]
print(str1[2:4])
print(str1[1:6])
print(str1[0:3])
print(str1[0:])
print(str1[1:5])

l1=["홍길동",100]
l2=[[2,3,5,],[4,5,6]]
l3=[True,[4,5,6],"hello",[1,2],3.14,5,]
print(l1,len(l1))
print(l2,len(l2))
print(l3,len(l3))

print(l2)
print(len(l2[0]))
'''
'''
#리스트명 추가
num=[0,1,2,3,4,5,6,7,8,9,10]
num.append(8)
num.append("숫자")
num.append([0,1,2])
print(num)

str1=["a","b","c","d","e","f"]
str1.append("ㄱ")
str1.append("ㄴ")
str1.append("ㄷ")
str1.append([1,2,3])
print(str1)

#list제거는 remove
num.remove(7)
print(num)

str1.remove("a")
str1.remove("c")
str1.remove("f")
print(str1)

#요소확인 
#in,not in
print(1 in num)

lan = ["영어","한국어","일본어", "스페인어", "중국어"]
print("영어" in lan)
print("한국어" not in lan)#참의 반대로 거짓이 나온다.
'''

tmp=[["미국","영국","일본","중국","스페인"],
    ["영어","일본어","중국어","스페인어"]]

print(tmp[1][1])

tmp[0][3]="대만"
print(tmp)

print(tmp[0][2:6])

tmp[0].append("프랑스")
tmp[1].append("프랑스어")
print(tmp)


