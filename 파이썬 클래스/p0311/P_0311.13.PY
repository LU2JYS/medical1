#함수선언
def stu_update(student): #지역변수 >주소값이 저장
    student["stuNo"]=2
    student["name"]="유관순"
    student["total"]=student["kor"]+student["eng"]+student["math"] #지역변수
    student["avg"]=student["total"]/3         #지역변수
    
    #리스트는 리턴이 없어서 바로 수정이 가능하다.
    #딕셔너리도 마찬가지이다
    




#딕셔너리 형태이다
#프로그램 구현
student={'stuNo': 1, 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 0, 'avg': 95.33}#리스트는 주소값이 저장이 되어있다.

#함수호출
stu_update(student) #전역변수 #리턴에 포함되 변수의 순서도 중요하다.

print("학생1: ",student)