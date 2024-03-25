import random
card_list = []
shape_list = ["spade","diamond","heart","clover"]
num_list = [0]*13
for i in range(1,14):
    num_list[i-1] = i
num_list[0] = "A"
num_list[10] = "J"
num_list[11] = "Q"
num_list[12] = "K"
# 카드 1세트를 구현해서 출력하시오.
card_list = [[0]*2 for i in range(52)]
cnt = 0
for i in shape_list: # "spade","diamond","heart","clover"
    for j in range(13):
        card_list[cnt] = {"shape":i,"num":num_list[j]}
        # print(card_list[cnt][0])
        # print(card_list[cnt][1])
        cnt += 1
    
random.shuffle(card_list)

arr_num=0
while True:
    print("1. 카드 1장 뽑기")
    print("2. 카드 5장 뽑기")
    print("0. 종료")
    c_num=input("번호를 선책해주세요.")
    print("현재 남은 카드 : ",len(card_list)-arr_num) #len(card_list)-arr_num
    #겹치지 않게 뽑기
    
    if c_num==1:
        print(card_list[arr_num]) #0
        print("모양:{},번호:{}".format(card_list[arr_num]["shape"],card_list[arr_num]["shape"]))
        arr_num+=1
    elif c_num ==2:
        for i in range(5):
            print("모양:{},번호:{}".format(card_list[arr_num]["shape"],card_list[arr_num]["shape"])) #1,2,3,4,5
            print()
            arr_num +=1
            
            

