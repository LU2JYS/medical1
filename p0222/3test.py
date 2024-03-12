#학생 이름, 국어,영어, 수학,점수를 입력받아서
# 아래와 같이 출력을 하고
#조거문 만약에 합격이다 하면 합격이라고 출력을 하시요

name=input("이름을 입력하시요")
kor=int(input("국어점수를 입력하시요"))
eng=int(input("영어점수를 입력하시요"))
math=int(input("수학점수를 입력하시요"))
total = kor+eng+math
avg =total/3

print("번호 \t이름\t국어\t영어\t수학\t합계\t평균\t등수")
print("{} \t{}\t{} \t{} \t{} \t{}  \t{} \t{}".format(
    1,name,kor,eng,math,total,avg,1))

if avg>85:
    print("홍길동님은 합격입니다")
else:
    print("불합격입니다ㅠㅠ")
    
print("-------------------------")
name=input("이름을 입력하시요")
kor=input("국어점수를 입력하시요")
eng=input("영어점수를 입력하시요")
math=input("수학점수를 입력하시요")
total = int(kor)+int(eng)+int(math)
avg =int(total)/3

print("번호 \t이름\t국어\t영어\t수학\t합계\t평균\t등수")
print("{} \t{}\t{} \t{} \t{} \t{}  \t{} \t{}".format(
    1,name,kor,eng,math,total,avg,1))

if avg>85:
    print("홍길동님은 합격입니다")
else:
    print("불합격입니다ㅠㅠ")