class Card: #4개의 변수가 있다. #사용자 정의 변수 #함수도 넣을수있다.
    kind=""
    number=""
    
    def __init__(self,kind,number):
        self.kind=kind 
        self.number=number
        
        
#클래스를 이용해서 52장의 카드생성       
c_list=[] #카드 리스트에 담아 52장 카드 출력하기>>>>>>>>>
kind = ["Spade","Diamond","Heart","clover"]
number=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

for i in range(4):
    for j in range(13):
        c=Card(kind[i],number[j]) #클래스형태로 담음/데이터보안에 강함/grouping이 됨
        c_list.append(c)
        
for i in range(52): 
    print("카드 출력 : ",c_list[i].kind,c_list[i].number) 
    

# #카드 리스트에 담아 52장 카드 출력하기>>>>>>>>>
# c_list=[] 
# kind = ["Spade","Diamond","Heart","clover"]
# number=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
# for i in range(4):
#     for j in range(13):
#         c=[kind[i],number[j]] #리스트를 생성해 리스트에 추가/데이터보안에 취약(몇번째 방이라고 불리어짐)
#         c_list.append(c)
        
        
# for i in range(4):
#     for j in range(13):
#         print("카드 출력 : ",kind[i],number[j])        

# c1=Card("","")    
# c1.kind="spade"
# c1.number=5
# print(c1.kind,c1.number)

# #c2 "heart","A"
# #모양을 DIAMOND 변경후 출력하시요
# c2=Card("heart","")    
# c2.kind="DIAMOND"
# c2.number="A"
# print(c2.kind,c2.number)

