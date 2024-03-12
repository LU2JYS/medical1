student = []
stu1=["홍길동"]
stu2=["유관순"]
student=[stu1,stu2]
kor1=int(input("첫번째 학생의 국어점수를 입력해주세요"))
eng1=int(input("첫번째 학생의 영어점수를 입력해주세요"))
math1=int(input("첫번째 학생의 수학점수를 입력해주세요"))
kor2=int(input("두번째 학생의 국어점수를 입력해주세요"))
eng2=int(input("두번째 학생의 영어점수를 입력해주세요"))
math2=int(input("두번째 학생의수학점수를 입력해주세요"))

print("{}\t{}\t{}\t{}".format(student[0],kor1,eng1,math1))

print("{}\t{}\t{}\t{}".format(student[1],kor2,eng2,math2))

#stu1=["",0,0,0] >>>>이런식으로 기본값을 설정하고 리스트에서 찾아 넣을수있다.