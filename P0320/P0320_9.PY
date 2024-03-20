def jecob(val):
    return val ** 2

def func(val):
    return val >= 3

def int_change(val):
    return int(val)


a_list = [1, 2, 3, 4, 5]
str_list = ["1", "2", "3", "4", "5"]
# map 함수를 사용하여 각 요소에 jecob 함수 적용
map_list = map(jecob, a_list)

# map_list를 리스트로 변환하여 출력
print(list(map_list)) #리스트 전체에 값의 변경이 필요할때

ss_list=list(map(int_change,str_list))
print(str_list) #문자열로 출력
print(ss_list) #숫자로 출력

ss_list2=list(map(lambda val:int(val),str_list))
print(ss_list2) #숫자로 출력


f_list = list(filter(func,a_list))
print(f_list) # 조건에 맞는 값만 출력할때