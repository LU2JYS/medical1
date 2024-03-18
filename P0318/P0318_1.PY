
# class(클래스)= 사용자정의 변수이다 .=함수도 포함.
#클래스 다음 글자는 대문자를 사용해야한다. Car


#  클래스 설계도
class Car:
    color = "white"
    door = 5
    length = 4710
    width = 1800
    displace = 1600
    speed =0
    
    def upSpeed(self,sp):
        self.speed += sp
        
    def downSpeed(self,sp):
        self.speed -= sp
        
#c1,c2는 객체가 다르다 >>제품car가 한개씩생산     
#<<<<<<<<<<<<<<<<따로따로 정보가 들어가서 별개이다>>>>>>>>>>>>>
c1=Car() #객체선언 무조건 앞에 대문자선언 Car
print("색상:",c1.color)
c1.color="red"
print("변경후 색상:",c1.color)

c2=Car()
print("색상:",c2.color)
    
#--------------------------------------------------------
def func(): #함수도 선언이 된다.
    pass

c1=Car() #클래스 객체선언 :car클래스에 있는 모든 변수를 사용함
print(c1.color)  

c2=Car()
print(c2.door) 

c3=Car()



