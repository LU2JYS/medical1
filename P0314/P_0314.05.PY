numbers=[1,2,3,4,5,6,7,8,9,10]

#인덱스는 리스트에 존재하면 위치값을 리턴
print(numbers.index(5))
try:
    print(numbers.index(9))
except Exception as a:
    print(numbers.index(11))
    print(a)



if 11 in numbers:
    print("7은 리스트에 존재합니다")
else:
    print("7은 리스트에 없습니다.")