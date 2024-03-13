#매개변수 순서 중요, 매개변수 타입도중요



def str_print(txt,num):
    for i in range(num):
        print(txt,end="")
        
        
    
txt=input("출력하고 싶은 글자를 입력하세요")
num=int(input("출력하고 싶은 글자의 반복횟수를 입력하세요>>>"))
str_print(txt,num)

# 안녕하세요
# 반복이 3번이면
# 안녕하세요 안녕하세요 안녕하세요.