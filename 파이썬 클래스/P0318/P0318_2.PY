


class Car: #<<<<<<<<<<<<<초기값 세팅은 이렇게 한다>>>>>>>>>
    c_name=""
    color=""
    door = 0
    lenght = 0
    width = 0
    speed = 0
    
    def up_speed(self,s): #클래스내에만 self를 넣어야 된다.!!!중요
        self.speed += s
        
c1=Car()
c1.c_name="포르쉐"
c1.color="red"
c1.door=5
c1.lenght=2000
c1.width=1000
c1.up_speed(60) #현재 스피드에서 60을 더해줌
c1.up_speed(40) #현재 스피드는 100 누적으로 위에서부터 아래로 누적이되어나온다.

print("철수의",c1.c_name,c1.color,c1.door,c1.lenght,c1.width,c1.speed)

c2=Car()
c2.c_name="벤틀리"
c2.color="black"
c2.door=2
c2.lenght=2500
c2.width=1500
c2.up_speed(60) #현재 스피드에서 60을 더해줌
c2.up_speed(40) #현재 스피드는 100 누적으로 위에서부터 아래로 누적이되어나온다.

print("영희의",c2.c_name,c2.color,c2.door,c2.lenght,c2.width,c2.speed)













# 철수=Car()
# print(철수.c_name,철수.color,철수.door,철수.lenght,철수.width,철수.speed)

# #영희의 차를 1대 생산해서, 색상은 green, 나머지 동일 ,speed=100출력하시요
# 영희=Car()
# 영희.c_name="영희의 더뉴 아반떼"
# 영희.color="green"
# 영희.speed=100
# print(영희.c_name,영희.color,영희.door,영희.lenght,영희.width,영희.speed)

# #반장의 차
# 반장=Car()
# 반장.c_name="반장의 디올 그랜져"
# 반장.lenght = 2500
# 반장.width = 2000
# 반장.color="화이트펄"
# 반장.speed=150
# print(반장.c_name,반장.color,반장.door,반장.lenght,반장.width,반장.speed)