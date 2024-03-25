#함수선언
def stu_update(student): #지역변수 >주소값이 저장
    student[0]=2
    student[1]="유관순"
    student[5]=student[2]+student[3]+student[4] #지역변수
    student[6]=student[5]/3         #지역변수
    
    #리스트는 리턴이 없어서 바로 수정이 가능하다.
    #딕셔너리도 마찬가지이다
    





#프로그램 구현
student=[1,'홍길동',100,100,100,0,0]#리스트는 주소값이 저장이 되어있다.

#함수호출
stu_update(student) #전역변수 #리턴에 포함되 변수의 순서도 중요하다.

print("학생1: ",student)