#함수선언
def stu_update(stuNo,name,kor,eng,math): #지역변수
    stuNo=2
    name="유관순"
    total=kor+eng+math #지역변수
    avg=total/3         #지역변수
    return total,avg,name,stuNo





#프로그램 구현
stuNo=1
name="홍길동"
kor=100
eng=100
math=100
total=0
avg=0

#함수호출
total,avg,name,stuNo =stu_update(stuNo,name,kor,eng,math) #전역변수 #리턴에 포함되 변수의 순서도 중요하다.

print("학생1: ",stuNo,name,kor,eng,math,total,avg)
