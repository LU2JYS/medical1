#number = input("숫자를 입력하시오") #input은 숫자,문자 상관없이 출력을 도와준다.
#print("입력하신 숫자는",number,"입니다")
#int는 숫자만을 표현할때 앞에 붙여줘야한다.

stu_no = input("번호을 입력하시요")
stu_name = input("이름을 입력하시요")
kor = input("국어 점수는?")
eng = input("영어 점수는?")
math = input("수학 점수는?")
print("번호",stu_no,)
print("이름",stu_name,)
print("국어",kor,)
print("영어",eng,)
print("수학",math,)
print("합계",int(kor)+int(eng)+int(math))
print("평균",(int(kor)+int(eng)+int(math))/3)
print("등수 1")
print("{} {} {} {} {} {} {}".format("번호","이름","국어","영어","수학","합계","평균"))
print(" {}  {}  {}  {}  {}  {}  {}".format("1", "홍길동", kor, eng, math, int(kor)+int(eng)+int(math), (int(kor)+int(eng)+int(math))/3))



