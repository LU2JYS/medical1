import operator

fruits=["바나나","바나나","바나나","딸기","배","사과","딸기","딸기","딸기","딸기","사과",
        "바나나","바나나","바나나","딸기","배","사과","딸기","딸기","딸기","딸기","사과"]
counter={}

for number in fruits:
    if number not in counter: #카운터 딕셔너리에 키값이 없으면
        counter[number] =0 #딕셔너리에 추가
    counter[number]+=1
    
print(counter) #그대로 출력
print(sorted(counter.items(),key=operator.itemgetter(1),reverse=True)) #뒤에 숫자 역순으로 출력
print(sorted(counter.items(),key=operator.itemgetter(1))) #뒤에 숫자 순차적으로 출력