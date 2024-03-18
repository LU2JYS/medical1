class Card: #4개의 변수가 있다.
    width=100 #클래스 변수
    height=200 #클래스 변수
    kind=""
    number=""
    
    def __init__(self,kind,number):
        self.kind=kind
        self.number=number
        Card.width=100
        Card.height=200
        
    def Card_print(self):
        print(f"Card : {self.kind},{self.number}")
        

card_list=[]
for i in range(13):
    card_list.append(Card("spade",i+1)) #밑에있는거랑 같다 심플!
    
# card_list.append(Card("spade","A")) #이게 위에 있는걸로 바꿀수잇다
# card_list.append(Card("spade","2"))
# card_list.append(Card("spade","3"))
# card_list.append(Card("spade","4"))
# card_list.append(Card("spade","5")
# card_list.append(Card("spade","6"))
# card_list.append(Card("spade","7"))
# card_list.append(Card("spade","J"))
# card_list.append(Card("spade","D"))
# card_list.append(Card("spade","K")))
print("리스트의 개수:",len(card_list))

for i in range(13): #밑에 있는거랑 같다
    print("리스트 출력 : ",card_list[i].kind, card_list[i].number)  

# print("리스트 출력 : ",card_list[0].kind, card_list[0].number)
# print("리스트 출력 : ",card_list[1].kind, card_list[1].number)
# print("리스트 출력 : ",card_list[2].kind, card_list[2].number)
# print("리스트 출력 : ",card_list[3].kind, card_list[3].number)
# print("리스트 출력 : ",card_list[12].kind, card_list[12].number)


card_list=[] #카드 리스트에 담아 52장 카드 출력하기>>>>>>>>>
shape = ["Spade","Diamond","Heart","clover"]
number=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
for i in range(4):
    for j in range(13):
        c=Card(shape[i],number[j])
        card_list.append(c)
        
        
for i in range(52):
    c= card_list[i] #카드객체
    print("카드 출력 : ",c.kind, c.number)
    
    


