import random


#카드종류 : spade,diamond,heart,clover 4종류
#카드숫자 : A,2,3,4,5,6,7,8,9,10,J,Q,K 13장 
#카드 총 수 : 52장

def card_creat(num_list):
    for i in range(1,14):
            num_list[i] = i
            num_list[0] = "A"
            num_list[10] = "J"
            num_list[11] = "Q"
            num_list[12] = "K"
            print(num_list)
            card_list = [[0]*2 for i in range(52)]
    cnt = 0
    for i in shape_list: # "spade","diamond","heart","clover"
        for j in range(13):
            card_list[cnt] = {"shape":i,"num":num_list[j]}
            cnt+=1
            
def card_suffle(card_list):
    pass

def card_share(card_list):
    pass

def card_print(card_list):
    pass


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
    shape_list=["spade","diamond","heart","clover"]
    num_list=[0]*13

    if choice==1:
        card_creat(num_list)
    
    elif choice ==2:
        random.shuffle(card_list)
        card_suffle()
    
    elif choice ==3:
        for i in range(5):
            print("모양:{},번호:{}".format(card_list[num]["shape"],card_list[num]["shape"])) #1,2,3,4,5
            print()
            num +=1
        card_share()
    
    elif choice ==4:
        
        card_print(num_list,card_list,shape_list)
    else:
        print("프로그램을 종료합니다")
        break

