import random

#클래스 선언 - 설계도
class Card: #4개의 변수가 있다.
    def __init__(self,kind,number):
        self.kind = kind
        self.number = number
        
kind_list=["spade","diamond","heart","clover"]
number_list=[1,2,3,4,5,6,7,8,9,10,11,12,13]
card_list=[] # 여기안에 52장의 카드가 있다.

#랜덤으로 1장 출력 함수로 출력
def random_one():
    num=random.randint(0,52)
    print("랜덤 카드 1장: ",num,card_list[num].kind,card_list[num].number)

#52장 카드 생성
for i in range(4):
    for j in range(13):
        card_list.append(Card(kind_list[i],number_list[j])) #카드 객체 선언
        
#52장 카드 출력        
for i in range(52):
    print("카드:",card_list[i].kind,card_list[i].number) #위에 def를 호출
    
#랜덤으로 1장 출력
random_one()

#랜덤카드 5장을 뽑는데 중복이 되지않게 하시요
#1. 0-51 순차적으로 정렬 (정렬섞기) 순차적으로 뽑으면 됨.
#2. 5장을 랜덤으로 뽑으면 된다.
#3. 1장 뽑고 기존에 있는 카드와 비교해서 다시 뽑는 방법

random_cards = random.sample(card_list, 5) #2번 방법
print("\n랜덤으로 선택된 5장의 카드:")
for card in random_cards:
    print(card.kind, card.number)
    
    
    