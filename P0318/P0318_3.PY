class Car: #<<<<<<<<<<<<<초기값 세팅은 이렇게 한다>>>>>>>>>
    c_name=""
    color=""
    door = 0
    lenght = 0
    width = 0
    speed = 0
    
    #생성자
    def __init__(self,c_name,color,door,lenght,width,speed):
        self.c_name=c_name
        self.color=color
        self.door=door
        self.lenght=lenght
        self.width=width
        self.speed=speed
        
    
    def up_speed(self,s): #클래스내에만 self를 넣어야 된다.!!!중요
        self.speed += s
        
# 생성자를 사용한 객체 =인스턴스 선언
#주문서를 넣어서 하는 방식
c1=Car("더 뉴 아반떼","white",5,200,1000,60) #저장값은 저장이되어있고 위치가 바뀌어도 저장값으로 변환
print("철수의",c1.c_name,c1.color,c1.door,c1.lenght,c1.width,c1.speed) 

c2=Car("더 뉴 아반떼","green",5,200,1000,100)
print("영희의",c2.c_name,c2.color,c2.door,c2.lenght,c2.width,c2.speed)








#기본생성자를 사용한 객체선언
# c1=Car()
# c1.c_name="포르쉐"
# c1.color="red"
# c1.door=5
# c1.lenght=2000
# c1.width=1000
# c1.up_speed(60) #현재 스피드에서 60을 더해줌
# c1.up_speed(40) #현재 스피드는 100 누적으로 위에서부터 아래로 누적이되어나온다.


# c2=Car()
# c2.c_name="벤틀리"
# c2.color="black"
# c2.door=2
# c2.lenght=2500
# c2.width=1500
# c2.up_speed(60) #현재 스피드에서 60을 더해줌
# c2.up_speed(40) #현재 스피드는 100 누적으로 위에서부터 아래로 누적이되어나온다.

# print("철수의",c1.c_name,c1.color,c1.door,c1.lenght,c1.width,c1.speed)
# print("영희의",c2.c_name,c2.color,c2.door,c2.lenght,c2.width,c2.speed)