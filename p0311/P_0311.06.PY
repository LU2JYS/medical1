sum=0

def plus(num):
    global sum
    sum+=num

    
n_input=int(input("숫자를 입력하세요>>>"))
plus(n_input)

print("총합:",sum)

def print_order(drink,cake):
    print("음료 :",drink, "/", "케익 :",cake)
print_order("아메리카노","치즈케익")