#자바같은 경우는 매개변수를 개수에따라 다른함수를 인정
#파이썬 이름이 무조건 달라야함

# def func(num1):
#     print(num1)
    
# def func(num1,num2,num3):
#     print(num1,num2)

# func(1)
# func(1,2)    #매개변수 개수가달라서 애러처리

def func2(num1,num2,num3=3): #키워드 매개변수 -값이 들어오지않으면 애러
    print(num1,num2,num3)
    
func2(100,2)