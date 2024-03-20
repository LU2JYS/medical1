class Car:
    count=0 #클래스변수로 일단 인식 공통공간이므로 통일
    
    def __init__(self,color="",speed=0): #생성자 함수이다(키워드변수)...!!!! #내부의저장되어있는 함수
        self.color = color #init 안에 변수선언 = 인스턴스 변수로 인신
        self.speed = speed
        
        # Car.count=0 #클래스 변수선언
        
        
#클래스 사용하기 위해서는 인스턴스 선언 무조건!!!!!!!!!!!!!!!!!!!        
c1=Car() #인스턴스 선언
c1.color="white"
c1.speed=50
print("c1.color: ",c1.color)
print("c1.speed: ",c1.speed)
Car.count=10
print("c1.count: ",c1.count) #클래스변수를 사용하려면 대문자 써야한다(Car)

#--------------------------------------------------------------------
c2=Car() #인스턴스 선언
c2.color="red"
c2.speed=70
print("\nc2.color: ",c2.color)
print("c2.speed: ",c2.speed)
Car.count=100
print("c2.count: ",c2.count)


# c2.count=30 >>>>>#기존 클래스변수를 지우고 새롭게 인스턴스변수를 다시 생성
# print(c2.count)

# c2.door=8 >>>>>>>>># 따로 추가가 가능하다!!>>>> 근데 하지마라!!!!
# print("c2.door:",c2.door)

