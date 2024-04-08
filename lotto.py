import random 

# 화면출력함수
def screen():
    print("[ 로또번호 맞추기 프로그램 ]")
    print("1. 번호생성")
    print("2. 번호섞기")
    print("3. 나의 로또번호입력")
    print("4. 번호확인")
    print("-"*30)
    choice = int(input("원하는 번호를 입력하세요.>> "))
    return choice

# 번호생성함수
def num_generate(lotto):
    print("[ 번호생성 ]")
    for i in range(45):
        lotto[i] = i+1
    print(lotto) 

# 번호섞기함수    
def num_shuffle(lotto):
    print('[ 번호섞기 ]')
    random.shuffle(lotto)
    print(lotto) 
    
def num_input(my_lotto):
    print("[ 나의 로또번호입력 ]") 
    for i in range(6):
        my_num = int(input(f"{i+1}번째 로또번호를 입력하세요.>>"))
        my_lotto[i] = my_num
    print("내가 입력한 번호 : ",my_lotto)   

def num_check(lotto,lucky_lotto,my_lotto,win_num,win_amount):
    for i in range(6):
        lucky_lotto[i] = lotto[i]
    print("[ 번호 확인 ]") 
    print("로또번호 : ",lucky_lotto)
    print("내가 입력한 번호 : ",my_lotto) 
    for i in my_lotto:
        if i in lucky_lotto:
            win_num.append(i)
    print("당첨된 번호 : ",win_num)  
    print("* 당첨금액 : {:,d} 원".format(win_amount[len(win_num)]))
    print("-"*40)
    print()

# 메인함수
def main():
    lotto = [0] * 45
    lucky_lotto = [0] * 6
    my_lotto = [0] * 6
    win_num = []
    win_amount = {0: 0, 1: 5000, 2: 10000, 3: 50000, 4: 100000, 5: 1000000, 6: 50000000}
    
    while True:
        choice = screen()
        
        if choice == 1:
            num_generate(lotto)
        elif choice == 2:
            num_shuffle(lotto)
        elif choice == 3:
            num_input(my_lotto)
        elif choice == 4:
            num_check(lotto, lucky_lotto, my_lotto, win_num, win_amount)
        else:
            print("올바른 선택이 아닙니다.")
            continue
        
        again = input("계속하시겠습니까? (Y/N): ")
        if again.upper() != 'Y':
            break

if __name__ == "__main__":
    main()
