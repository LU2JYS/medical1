import operator
numbers=[1,2,4,6,4,3,6,7,1,3,4,3,4,7,7,7,7,7,1,1,1]
counter={}
# counter["1"]=2
# counter["2"]=1
# print(counter)
#중복된 숫자를 나타내는 방법>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>카운트 방법
for number in numbers:
    if number not in counter: #카운터 딕셔너리에 키값이 없으면
        counter[number] =0 #딕셔너리에 추가
    counter[number]+=1 #딕셔너리를 1을 증가
    
    #많이 나온 숫자로 정렬하기
print(counter)
print(sorted(counter.items(),key=operator.itemgetter(0),reverse=True))
    