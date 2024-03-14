import random


#카드종류 : spade,diamond,heart,clover 4종류
#카드숫자 : A,2,3,4,5,6,7,8,9,10,J,Q,K 13장 
#카드 총 수 : 52장

def card_create():
    
            
def card_suffle():
    pass

def card_share():
    pass

def card_print():
    pass

c_shape=["spade","diamond","heart","clover"]
c_number=[0]*13
for i in range(13):
    c_number[i]=i+1
c_number[0]="A"
c_number[11]="J"
c_number[12]="Q"
c_number[13]="k"
#========================================
num=0
while True:
    print("[카드 프로그램]")
    print("1. 카드생성")
    print("2. 카드섞기생성")
    print("3. 카드5장 나눠주기")
    print("4. 카드5장 확인하기")
    print("0. 종료")
    print("-"*48)
    choice=int(input("원하는 번호를 입력하세요>>>"))
    card_list=[[0]*2 for i in range(52)]
    

    if choice==1:
        
    
    elif choice ==2:
        
    
    elif choice ==3:
        
    
    elif choice ==4:
        
        
    else:
        print("프로그램을 종료합니다")
        break

