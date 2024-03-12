score=[
    [80,90,85],[70,80,90],[84,92,80],[72,81,76]
]
name=["홍길동","유관순","이순신","김구"]
total=[]
#2.코딩
#2 하나하나 출력 ex)80 90....
#2 하나하나 출력된것을 다 더해서 total에 넣어주세요
# total=[255,240,256,226]
#3.출력
#3 total=[255,240,256,226]
#3 250미만 불합격 이상은 합격 ex)홍길동님은 합격입니다.


for i in range(len(score)):
    print(score[i])
    for j in range(len(score[i])):
        print(score[i][j])
    
    s=0
    for j in range(len(score[i])):
        s=s+score[i][j]
    total.append(s)
print(total)

for i in range(4):
    if total[i] >=250:
        print(" {} 합격입니다".format(name[i]))
    else:
        print(" {} 불합격입니다".format(name[i]))






