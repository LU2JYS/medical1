class Car: #<<<<<<<<<<<<<초기값 세팅은 이렇게 한다>>>>>>>>>
    car_no=0
    color=""
    door = 0
    tire=0
    speed = 0
    
    def up_speed(self,speed):
        self.speed += speed
    def down_speed(self,speed):
        self.speed -= speed 
        Car.car_no +=1
        
car_list = []
        
c1=Car()
c1.car_no=""
c1.color="white"
c1.door=5
c1.tire=4
c1.up_speed(30) 

car_list.append(c1)        

c2=Car()
c2.car_no=""
c2.color="red"
c2.door=5
c2.tire=4
c2.up_speed(100) 

car_list.append(c2)

c3=Car()
c3.car_no=""
c3.color="silver"
c3.door=5
c3.tire=4
c3.up_speed(70) 

car_list.append(c3)


for car in car_list:
    print(car.car_no,car.color, car.door, car.tire, car.speed)
print(car_list)    

