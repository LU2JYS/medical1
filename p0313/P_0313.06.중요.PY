import os

print("현재 운영체제 : ",os.name)
print("현재 폴더위치 : ",os.getcwd())
print("현재 폴더 내 파일들 표시 :",os.listdir())

# #폴더 생성
# os.mkdir("hello")
#폴더 삭제
# os.rmdir("hello")

#파일 생성
# with open("students.txt","w")as f:
#     f.write("1, '홍길동', 100, 100, 99, 299, 99.67,1")


#중요!!!!!!!!!!!!!!!!!!
#csv타입 >>>>>>>>>>>>>>중요 json 다른사람하고 공유가 가능하다
str1="1, '홍길동', 100, 100, 99, 299, 99.67,1"
s_list=str1.split(",")

for i in s_list:
    print(i)
