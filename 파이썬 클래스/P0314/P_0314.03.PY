# a_list=[1,2,3,4,5,6,7,8,"9",10]


# for i in a_list:
#     try:
#         print(i+1)  
#     except:
#         print("데이터오류가 있습니다.") #pass 넣어도된다.
        
        
        
        
print("프로그램 실행")
try:
    print(1)
    print(2)
    # print(1/0) #에러가 발생
    print(3)
except: #예외가 발생하면 실행
    print(4)
    print(5)
else: #예외가 발생하지 않으면 실행
    print(6)
finally: #예외가 발생하거나, 하지않거나 무조건 실행
    print(7)


print("프로그램 종료")
