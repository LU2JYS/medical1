fruits=["사과","복숭아","딸기","포도","배"]
#여기에 한라봉을 추가하고싶다
print("과일 리스트 :",fruits)
#리스트에 요소를 추가한다.
fruits.append("한라봉")# >>>>>>>> 추가할때 사용 많이한다.
print("추가된 리스트 :",fruits)
fruits.append("체리") 
print("추가된 리스트 :",fruits)
fruits.remove("사과") #remove는 제거할수있는 효과가있다.
print("추가된 리스트 :",fruits)

if "딸기" in fruits:
    print("딸기가 있습니다.")
else:
    print("딸기가 없습니다.")
    
temp =[]
print(temp)
temp.append(1)
print(temp)
temp.append(2)
print(temp)
temp.append("홍길동")
print(temp)

# 변수
a=2
b=3
c=a+b
print("{}+{}={}".format(a,b,c))

l1=[1,2,3,4,5]
a1=2
b1=3
print("{}+{}={}".format(l1[1],l1[2],l1[4]))

#list li에 있는 숫자들의 합을 구해보시오
result=l1[0]+l1[1]+l1[2]+l1[3]+l1[4]
print(result)