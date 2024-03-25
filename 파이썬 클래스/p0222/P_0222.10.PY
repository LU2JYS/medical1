n=int(input("숫자를 입력하세요"))
if n >=100:
    print("100보다 크거나 작습니다")
else:
    print("100보다 작습니다")
    



print("----------------")
n=int(input("숫자를 입력하세요"))
if n  % 2==0 : #짝수인경우 짝수로 출력 아니면 홀수>>>중요!!!!
    print("짝수입니다.")
else:
    print("홀수입니다.")

print("----------------")
n=int(input("숫자를 입력하세요"))
if n >= 60 :
    print("합격입니다.")
else:
    print("불합격입니다.")
    
print("----------------")
n=int(input("숫자를 입력하세요"))
if 5<n<10: #if 5 < n and n < 10:  같은 경우이다
    print("5보다 크고 10보다 작은수입니다")
else:
    print("숫자가 벗어납니다")
    
print("----------------")
n=int(input("숫자를 입력하세요"))
if 3*n:
    print("3의 배수입니다")

print("----------------")    
n=int(input("숫자를 입력하세요"))
if n*2 and n*3 :
    print("2의 배수이며 3의 배수이기도 하다")