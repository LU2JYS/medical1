# 변수 3개를 만들어서 name, city, fruit

#변수선언
name ="전용성"
city = "서울시"
fruit = "포도"

#출력
print("저의 이름은",name,"입니다.")
print("나는 ",fruit,"를 좋아합니다.")
print("저는",city,"에서 태어났습니다.")

print("-----------------")
print("나의 이름은 %s입니다"%name)
print("내가 좋아하는 과일은 %s입니다"%fruit)
print("내가 태어난곳은 %s입니다"%city)


print("-----------------")
name=input("이름을 입력하시오>>>") #input은 내가 입력한 값을 변수로 생각한다.
city=input("사는곳을 입력하시오>>>")
fruit=input("좋아하는 과일을 입력하시오>>>")
print("나의 이름은",name,"입니다")
print("내가 사는곳은",city,"입니다")
print("내가 제일 좋아하는 과일은",fruit,"입니다")


