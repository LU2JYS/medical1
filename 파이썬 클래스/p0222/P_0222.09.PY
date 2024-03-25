#조건문 반복문 일때 들여쓰기를 실행해야한다...>>>>>>>중요
#if
#if-else
#else
a=99 # a에 99대입
if a < 100 :
    print("a는 100보다 작습니다")
    
print("프로그램을 종료합니다.")

str1="banana"
print('if시작')
if str1 =="banana":
    print("먹는다")
    print("바나나")
print("종료")

name=10
if name == 10 :
    print('10입니다')
else:
    print("10이 아닙니다.")
    
name=101
if name != 100 :
    print('100이 아닙니다.')

print("----------------")
name=10
if name >= 10 :
    print('10보다 크거나 같습니다')
else:
    print("10보다 작습니다")
    
print("----------------")
n=-10
if n>0:
    print("양수입니다")
else: 
    print("음수입니다")
    
print("----------------")
n=int(input("숫자를 입력하세요"))
if n>0:
    print("{}양수입니다".format(n))
else: 
    print("{}음수입니다".format(n))