num=int(input("월을 입력하세요"))
num1 =num[0:-1]
print(num1)
if num in [12,1,2]:
    print("겨울 입니다")
elif num in [3,4,5]:
    print("봄 입니다")
elif num in [6,7,8]:
    print("여름 입니다")
else:
    print("가을입니다")
    



