from telnetlib import PRAGMA_HEARTBEAT


class Car:
    count=0

    def __init__(self,color="white",door=5,speed=0,tire=4):
        self.color=color
        self.door=door
        self.speed=speed
        self.tire=tire #기본 옵션들이다
        
    def up_speed(self):
        self.speed +=10
        
    def down_speed(self):
        self.speed -=10  
        
    def stop_speed(self):
        self.speed -= 10  
        
#Car클래스 상속 >>>  (기본옵션이 그대로 상속이된다)
class Ambul_car(Car):
    
    def up_speed(self):
        self.speed +=20 #오버라이딩 이라고 한다. 새로 정의한것이다.
        # return super().up_speed()
        
    def up_speed2(self): #기존 부모의 함수를 다시 호출할때
        return super().up_speed() #부모의 요소를 가져올때  super()
        
    def siren(self):
        print("싸이렌이 울리는 기능이 있다.")
        
        
#Car클래스 상속 >>>  (기본옵션이 그대로 상속이된다)  
class FireTruck_car(Car):
    
    def water(self):
        print("물을 뿌리는 기능이 있다.")
        
a1=Ambul_car()
print("현재속도 :",a1.speed)
a1.up_speed()              # 자식의 오버라이딩 된 함수를 호출
print("현재속도 :",a1.speed)
a1.up_speed2  #부모의 함수를 호출
print("현재속도 :",a1.speed)
a1.stop_speed()
print(a1.speed) #스피드가 -10으로됨

# # a2= Ambul_car()
# print(a2.color,a2.door,a2.speed,a2.tire)
