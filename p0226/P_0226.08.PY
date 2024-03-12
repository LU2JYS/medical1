#반복문
print("안녕하세요"*5)
'''
for 변수 in 반복가능한 데이터:
수행할 문장
'''
'''
for i in range (0,6,1): #range(시작값, 끝값+1, 증가값)>>>>>>중요
    print(i,"안녕")
    
for i in range (0,3): #증가값이 1인경우 생략가능
    print(i,"hi")
    
for i in range (4): #n번 반복할경우의 range를 사용할수있다.
    print(i,"hello")
for _ in range (2): #i를 사용하지 않고 _사용가능
    print("반갑습니다")
    
for i in range(5): #>>>>>>>>>>>>중요
    num = int(input("숫자를 입력해주세요"))
    print("입력하신 숫자는 :{}".format(num))
    '''
    #i,j 카운터 변수 ,k,l 등등있다
    #카운터 변수는 반복실행 할때마다 현재 실행 횟수에 해당되는 숫자가
    #들어감 ,가장 처음은 실행한적이 없으므로 0이된다.
'''
for i in range(3):
    print(i)
    
str1="안녕하세요"
for i in str1:
    print(i)
'''

for i in range(1,16,1):
    print(i)
    
for i in range (4):
    print(i,"10")
    
for i in range (6):
    print(i,"helloworld")
    
for i in range (0,101,2):
    print(i, end=", ")
print()#줄 바꿈이 되어 들어간다 (빈공백)
for i in range (0,101,5):
    print(i, end=", ")   
