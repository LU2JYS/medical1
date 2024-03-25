#continue : 반복문에서 남은 문장을 수행하지 않고 다음단계로 넘어감
'''
n=0
while n< 100:
    n+=1
    if n%2==0:
        continue
    print(n,end=" ")

#continue는 문자를 건너띄고 출력이됨

#pass 문자를 만나면 어떠한 동작도 안한다
'''
'''
i=0
sum=0
while i <101:
    i+=1
    if i%3==0:
        continue
    sum+=i
    print(i,end=" ")
print(sum)
'''
from random import*
#랜던함 숫자를 만들어서 (1-100사이)
#내가 입력한 값이 랜던ㅁ한 숫자랑 같으면 당첨(프로그램 종료)
#아니면 다시 입력하세요 뜨기
print(randint(1,100))
print(randint(1,100))
print(randint(1,100))
print(randint(1,100))
print(randint(1,100))
#현재 입력한 숫자 모두를 inputlist에 넣기
inputlist=[]
#10회 도전 후 프로그램 종료
randnum=randint(1,100)
cnt=0
while cnt<10: 
    userInput=int(input("숫자를 입력해주세요"))
    inputlist.append(userInput)
    if randnum ==userInput: 
        print("당첨") 
        break
    elif userInput > randnum: 
        print("더 큰수를 입력해주세요")
        print("더 큰수를 입력해주세요",randnum)
    else:
        print("더 작은수를 입력해주세요")
        
if cnt ==10:
    print("10회 입력을 초과하였습니다. 정답은",inputlist)

    
    

