import operator #클래스를 정렬하는것이다.


#딕셔너리 정렬
t_dic={}
t_list=[]
t_dic={"peach":"복숭아","orange":"오렌지","apple":"사과",
        "pear":"배","grapes":"포도","mango":"망고","kiwi":"키위"}

# print(t_dic.keys()) # key값
# print(t_dic.values()) # value값
# print(t_dic.items()) # 튜플

# print(sorted(t_dic.items(),key=operator.itemgetter(0))) #영어로 정렬
print(sorted(t_dic.items(),key=operator.itemgetter(1))) #keys값 으로정렬 뒤에 한글로 정렬
# print(sorted(t_dic.items(),key=operator.itemgetter(0),reverse=True)) >>영어 역순으로
# print(sorted(t_dic.items(),key=operator.itemgetter(1),reverse=True)) >>한글 역순으로
# (preach,복숭아).(orange,오렌지)






a=[5,7,4,8,1,9,3,2]
a.sort() #순차적으로 정렬한다.
print(a)

b=[5,7,4,8,1,9,3,2]
b.sort(reverse=True) #역순으로 프린팅이 된다.
print(b)

'''
# 3개의 숫자를 입력받아 순서대로 출력하세요
# 17,,50,12
# 12,17,50
num=[0,0,0]
for i in range(3):
    print(i)
    num[i]=int(input(f"{i+1}번째 숫자를 입력하세요>>>")) #f는 format이다>>>
    #input("{}번째 숫자를 입력하세요".format(i+1)) 같은 방법이다.>>>>
num.sort() #순차적으로 출력을 도와준다.
print("최대값: ",max(*num)) #가장 큰값을 보여준다
print("최소값: ",min(*num)) #가장 작은값을 보여준다
print(num)
'''