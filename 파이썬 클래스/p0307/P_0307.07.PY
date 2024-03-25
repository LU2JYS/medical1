import random

fruit={"peach":"복숭아","orange":"오렌지","apple":"사과",
        "pear":"배","grapes":"포도","mango":"망고","kiwi":"키위"}


f_list=list(fruit.keys()) #키값만 있으면 된다
print(f_list)

#랜덤으로 뽑아보자
f_list_ram= random.sample(f_list,4)
print("랜덤추출:",end=":")
for f in f_list_ram:
    print(fruit[f],end=",")









'''
print(fruit["peach"]) #>>>>>>>>>>>>>키값넣으면 value값이 나온다!!!!
print(fruit["kiwi"]) #>>>>>>>>>>>>>키값넣으면 value값이 나온다!!!!

f_list=["peach","pear","kiwi"]

print(fruit[f_list[2]]) #>>>>>>>>>>>>>지정 위치값만 빼오기

for f in f_list:
    print(fruit[f])  #f_list 리스트에만 있는거 빼오기
'''