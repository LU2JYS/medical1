#가변 매개변수

def str_title(num,*txt):
    for i in range(num):
        for t in txt:
            print(t)
        print()    
        
    
str_title(3, "안녕","잘가","반갑습니다","사랑해요")