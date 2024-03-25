import random

w_list=["토마토","바나나","사과","배","수박","메론","복숭아"]

#random에 랜덤하면
#0-1사이에 실수를 랜덤실수 생성 0.0000000-0.999999999
print(random.random())


#정수형 타입의 숫자를 랜덤하게 생성해준다.0-10까지
print(random.randint(0,10)) 

#0-3까지만 출력해준다>>마지막숫자 앞까지만 출력
print(random.randrange(0,3))

#리스트를 랜덤으로 섞어준다.
list=[1,2,3,4,5,6,7]
random.shuffle(list)
print(list)


#리스트에서 숫자 1개를 랜덤으로 추출
print(random.choice(list))

#리스트에서 해당되는 숫자만큼 랜덤으로 추출>>>>>중복은 불가능
print(random.sample(list,4))

w_list=["토마토","바나나","사과","배","수박","메론","복숭아"]
print(random.sample(w_list,3)) #리스트에서 가져온다.


fruit={"peach":"복숭아","orange":"오렌지","apple":"사과",
        "pear":"배","grapes":"포도","mango":"망고","kiwi":"키위"}
print("갯수:",len(fruit))
#랜덤으로 4개만 출력
#랜덤은 리스트만
#key를 리스트 타입으로 변경
print(fruit.keys())

f_list=random.sample(list(fruit.keys()),4)

f_list2=["kiwi","grapes","peach","pear"]

print(fruit[f_list2[0]])


#value 값을 전체 출력
for key in fruit:
        print(fruit[key])
