#if -else 를 배워왓다
#if - elif - else
'''
if 조건문1 :
    실행문1
elif 조건문2 : 
    실행문2
else:
    실행문3
    
조건문1이 참이면 실행문 1 실행 후 종료
조건문1이 거짓이고 조건문2가 참이면 실행문2 실행후 종료
조건문1, 조건문2가 거짓이면 실행문3 실행후 종료
'''    
'''
weather="비"
if weather =="비":
    print('비가 오네요 우산을 챙겨주세요')
elif weather=="눈":
    print("눈이 오네요 우산을 챙겨주세요.")
else:
    print("썬크림을 챙겨주세요")
'''
n=10
if n>0:
    print('양수입니다')
elif n<0:
    print("음수입니다")
else:
    print("0입니다")
    
m=int(input("금액을 써주세용>>>"))    

if m>=10000:
    print("택시를 탄다")
elif m>=2000:
    print("버스를 탄다")
elif m>=1000:
    print("따릉이를 빌린다")
else:
    print("걸어간다.")