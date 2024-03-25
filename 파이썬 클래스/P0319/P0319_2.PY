class Car: #<<<<<<<<<<<<<초기값 세팅은 이렇게 한다>>>>>>>>>

    def __init__(self,color,door,tire,speed) :
        self.color=color
        self.door=door
        self.tire=tire
        self.__speed=speed #클래스 내부에서만 가능하다(접근제한)(캡슐화 방법)
    
    def up_speed(self):
        self.__speed += 10

    def down_speed(self):
        self.__speed -= 10 
        
    def get_speed(self):
        return self.__speed 
    
    def set_speed(self,speed):
        self.__speed += speed  # 이렇게 설정하면 바로 접근이 가능하다  
        
c1=Car("white",5,4,0) #speed 0
c1.up_speed()         #speed 10
c1.up_speed()         #speed 20
c1.set_speed(500) # 이렇게 설정하면 바로 접근이 가능하다

# c1.up_speed = 500 # 이렇게 설정하면 바로 접근이 불가능하다

#클래스의 변수에 직접적으로 접근이 안됨
#get을 통해서만 접근이 가능
print(c1.get_speed())

c2=Car("red",4,4,0)
