# 중첩 if

'''
a=97
if a  > 90:
    print("a가 90보다큽니다")
    else:
    print("90보다 작습니다")
    if a  > 90:
    print("90보다 작습니다")
    if a<95:
    print("95보다 큽니다")
else:
    print("90보다 작습니다")'''
    
#만약 사과의 상태가 good이며
#1000원 이하이면 [10개 구매]
#1000원보다 비싸면 [3개 구매]를 출력 
# 사과의 상태가 "good"이 아니면 [사과를 구매하지않는다]
apple="bad"
price=1500

if apple == "good":
    print("구매합니다")
else:
    print("구매 하지 않는다")
if price <= 1000:
    print("10개를 구매")
else:
    print("3개를 구매")
    
#숫자 하나를 입력받아서
# 100보다 큰면서 짝수면 짝수, 홀수이면 홀수
#100보다 작으면 100보다 작다라고 출력

num=int(input("숫자를 입력하시요"))

if num > 100 :
    print("100보다 크다")
    if  num %2==0:
        print("100보다 크면서 짝수")
    else:
        print("100보다 크면서 홀수")
else:
    print("100보다 작다")
    
