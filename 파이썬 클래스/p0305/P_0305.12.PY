foods={"떡볶이":"오뎅","짜장면":"단무지","라면":"김치",
        "피자":"피클","맥주":"땅콩","삼겹살":"상추"}


#키의 값을 출력하세요.
print(foods.keys()) #앞의값이 출력

#value의 값을 출력하세요.
print(foods.values()) #뒤의값이 출력

#키:value 형태 모두 출력하세요.
print(foods.items()) #모두 출력
for key in foods:
    print(f"{key}:{foods[key]}")

