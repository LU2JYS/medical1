class Car:
    car_no = 0  # 클래스 변수
    def __init__(self, color, door, tire):
        Car.car_no += 1
        self.car_no = Car.car_no
        self.color = color
        self.door = door
        self.tire = tire
        self.speed = 0
    def up_speed(self, speed):
        self.speed += speed
    def down_speed(self, speed):
        self.speed -= speed
    def __str__(self):
        return f"{self.car_no},{self.color},{self.door},{self.tire},{self.speed}"
# Car 객체 생성 후 리스트에 추가
car_list = []
c1 = Car("white", 5, 4)
c1.up_speed(30)
car_list.append(c1)
c2 = Car("red", 5, 4)
c2.up_speed(100)
car_list.append(c2)
c3 = Car("silver", 5, 4)
c3.up_speed(70)
car_list.append(c3)
# 리스트 출력
for car in car_list:
    print(f"Car Number: {car.car_no}, Color: {car.color}, Door: {car.door}, Tire: {car.tire}, Speed: {car.speed}")
print(car_list)