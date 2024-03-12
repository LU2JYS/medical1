today_list=["2024","03","08"]
# today_list[0]=int(today_list[0])+10
# print(today_list)


#리스트에있는 문자열을 인트(숫자로)로 변경해서 리스트에 넣어라
print(today_list)
t_list=list(map(int,today_list)) 
print(t_list)

#map은 정수형을 문자열로 모두 변환해서 리스트에 저장
int_list =[10,20,30,40,50]
str_list=list(map(str,int_list)) #int를 str(문자)형태로 바꿈>>>>>>>>>>>>>>
print(str_list)

# list=[]
# for i in range(5):
#     list.append(i) #리스트에 int타입으로 들어간다.
# print(list)

#리스트의 인트타입을 str타입으로 바꾸자
a_list=list(map(int,input("숫자를 입력하세요:"))) #문자열로 바뀌었다.
print(a_list)







#5개의 숫자를 입력하세요
# list=[]
# for i in range(5):
#     list(map(int,input("숫자를 입력하세요"))) #
#     # list.append(int(input("숫자를 입력하세요")))
# print(list)