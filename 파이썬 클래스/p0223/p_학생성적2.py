

#입력받아서 총점과 평균을 계산하고

#출력하세요

stu_name=input("학생 이름을 입력하시요")
kor=int(input("국어점수를 입력하세요 "))
eng=int(input("영어점수를 입력하세요"))
math=int(input("수학점수를 입력하세요"))
sum=kor+eng+math
avg=kor+eng+math/3
print("번호 \t이름\t국어\t영어\t수학\t합계\t평균\t등수")
print("{}\t{}\t{} \t{} \t{} \t{}  \t{:.1f} \t{}".format(
    1,stu_name,kor,eng,math,sum,avg,1))

