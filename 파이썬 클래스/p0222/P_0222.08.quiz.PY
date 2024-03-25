print("-"*35)
print("\t[학생성적프로그램]")
print("-"*35)
print("1. 학생성적입력")
print("2. 학생성적수정")
print("3. 학생성적삭제")
print("4. 학생성적 전체 출력")
print("5. 학생검색출력")
print("6. 등수처리")
print("0. 프로그램종료")
print("-"*35)

print("번호 \t이름\t국어\t영어\t수학\t합계\t평균\t등수")
print("{} \t{}\t{} \t{} \t{} \t{}  \t{} \t{}".format(
    1,"홍길동",100,100,100,300,100.0,1
    ))
print("번호 \t이름\t국어\t영어\t수학\t합계\t평균\t등수")
print("{} \t{}\t{} \t{} \t{} \t{}  \t{} \t{}".format(
    2,"유관순",90,100,90,300,100.0,1
    ))

#홍길동 100 100 100
#유관순 90 100 90 
name1=input("첫번째 이름을 입력하시요")
name2=input("두번째 이름을 입력하시요")
kor1=input("첫번째 학생의 국어 점수를 입력하시요")
kor2=input("두번째 학생의 국어 점수를 입력하시요")
eng1=input("첫번째 학생의 영어 점수를 입력하시요")
eng2=input("두번째 학생의 영어 점수를 입력하시요")
math1=input("첫번째 학생의 수학 점수를 입력하시요")
math2=input("두번째 학생의 수학 점수를 입력하시요")
sum1 = int(kor1)+int(eng1)+int(math1)
sum2 = int(kor2)+int(eng2)+int(math2)
avg1 = (int(sum1)/3)
avg2 = (int(sum2)/3)

print("번호 \t이름\t국어\t영어\t수학\t합계\t평균\t등수")
print("{} \t{}\t{} \t{} \t{} \t{}  \t{} \t{}".format(
    1,name1,kor1,eng1,math1,sum1,avg1,1
    ))
print("{} \t{}\t{} \t{} \t{} \t{}  \t{:.2f} \t{}".format(
    2,name2,kor2,eng2,math2,sum2,avg2,2
    ))