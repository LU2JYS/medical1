#split 은 문자열 분리를 도와준다.

hobby="게임,골프,독서"

#리스트타입으로 정렬
print(hobby.split(","))  #리스트안에서도 한개씩 분리된다.


# 두가지 방법이 있다..>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
h_data="23-10-23,1,강원도 강릉시,강릉동인병원,383,21,033)651-6167,강릉대로419번길 42,종합"
h_list=h_data.split(",")
print("병상수: ",h_list[4]) #리스트에 위치를 지정해주고 가져올수있다.

a_data="23-10-23/1/강원도 강릉시/강릉동인병원/383/21/033)651-6167/강릉대로419번길 42/종합"
a_list=a_data.split("/")
print("병상수 :",a_list[4])

ss="%"
print(ss.join("파이썬")) #문자 사이사이에 넣어준다

s_data="2023/03/08"
s_data_list=s_data.split("/")
print(s_data_list)

s_time ="2023:03:08:16:48:00"
s_time_list=s_time.split(":")
print(s_time_list)

print("-"*50)

today = "2024/03/08" #문자열로 넘어왓다
#10년후의 날짜를 입력하세요 2034/03/08
t_list=today.split("/") #>>>>>>>>>>>>>>>>>>>반드시 알아두자 중요!!!!!!!!!!
t_list[0]=int(t_list[0])+10
today2="{}/{}/{}".format(*t_list)
print(today2)



















