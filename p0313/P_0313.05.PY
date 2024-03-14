# import random


from random import* #  *은 모든것.

#0.00000000000-0.9999999999 랜덤으로 소수점의 결과값 리턴
print(random.random())

# print(random.uniform(10,20)) #10-20사이를 랜덤으로 돌려준다

# #1-2까지 랜덤으로 출력
# print(random.randrange(1,3))\

# #리스트 내에 1개만랜덤 선택
# print(random.choice([1,2,3,4,5]))


# #리스트의 요소를 랜덤으로 섞음
# a_list=[1,2,3,4,5]
# random.shuffle(a_list)
# print(a_list)

# #리스트 내에 2개만 랜덤 선택
# print(random.sample([1,2,3,4,5],k=2)) #<< k= 여기서 선택 개수를 입력하면됨(안에 리스트 개수랑 다르면 애러)



# #1-10 10을 포함,>>>>>범위 내 랜덤 int를 선택
# print(random.randint(1,10))



# # import math

# # print(math.sin(1))
# # print(math.cos(1))
# # print(math.tan(1))

