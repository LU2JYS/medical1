students=[[1,"홍길동",100,100,99,299,99.97],
        [2,"유관순",100,100,99,299,99.97],
        [3,"이순신",100,100,99,299,99.97]]

while True:
    search = input("찾는 학생의 이름을 넣으세요")
    chk=0
    count=0
    for stu in students:
        if search in stu:
            chk=1
            break
        count+=1 #찾는 학생의 위치값
    if chk==0:
        print("찾는 학생이 정보가 없습니다.")
    else:
        print("입력한 학생이름 {}을 찾았습니다.".format(search))
        print("[변경할 과목 선택]")
        print("1. 국어 2. 영어 3. 수학 0. 취소")
        
        num=int(input(">>")) 
        if num ==1:
            print("국어를 선택하였습니다.")
            print("현재 국어점수: ",students[count][2])
            num=int(input("변경할 점수를 입력해주세요"))
            students[count][2]=num
            print("국어점수가 변경되었습니다.")
            #합계,평균도 수정
            total=students[count][2]+students[count][3]+students[count][4]
            students[count][6]=float("{:.2f}".format(students[count][5]/3)) #문자열이다(float으로 바꾸거나),#만약에 int하면 소숫점이 날라간다...
            
        elif num ==2:
            print("영어를 선택하였습니다.")
            print("현재 영어점수: ",students[count][3])
            num=int(input("변경할 점수를 입력해주세요"))
            students[count][3]=num
            print("영어점수가 변경되었습니다.")
            #합계,평균도 수정
            total=students[count][2]+students[count][3]+students[count][4]
            students[count][6]=float("{:.2f}".format(students[count][5]/3)) #만약에 int하면 소숫점이 날라간다...
            print(students)
            #성적 수정 프로그램 구현
            
        elif num ==3:
            print("수학를 선택하였습니다.")
            print("현재 수학점수: ",students[count][4])
            num=int(input("변경할 점수를 입력해주세요"))
            students[count][4]=num
            print("수학점수가 변경되었습니다.")
            #합계,평균도 수정
            total=students[count][2]+students[count][3]+students[count][4]
            students[count][6]=float("{:.2f}".format(students[count][5]/3))
            print(students)
            #성적 수정 프로그램 구현
            print("성적을 취소를 선택하였습니다.")
        
        else:
            print("취소하였습니다.")
            #성적 수정 프로그램 구현