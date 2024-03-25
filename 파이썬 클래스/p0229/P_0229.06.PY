'''
while True:
    n=input("원하는 번호를 입력하세요")
#n은 문자열
    if n.isdigit(): #숫자지만 문자열인것 예: "0","1"
        n=int(n)
    else:
        print("문자가 입력되었습니다.다시 입력해주세요")
    if n ==0:
        print("숫자 0이 입력되었습니다.")
'''    
#이름을 검색해보고, 이름을 검색해서 삭제해보기
students=[[1,"홍길동,100"],[2,"이순신",90],[3,"유관순",85],
        [4,"김유신",70],[5,"김구",95]]
while True:
    print("1. 학생 검색")
    print("2. 학생 삭제")
    print("3. 프로그램이 종료")
    ch= input("원하는 번호를 입력해주세용>>>")
    if ch.isdigit(): #입력한게 숫자이면 true
        ch=int(ch)   #입력한 숫자가 나오게끔 해준다.    
    if ch==1:
        searchName=input("원하는 학생를 입력해주세용>>>")
        chk=0
        for stu in students:
            print(stu)
            if searchName in stu:
                print(stu)
                chk=1
                print(delName,"학생이 삭제 되었습니다.")
        if chk==0:
            print("검색하신 학생이 존재하지않아요")   
        print(students)    
    elif ch==2:
        delName =input("삭제하고 싶은 학생의 이름을 입력하세요.")
        for i, stu in enumerate(students):
            if delName in stu:
                del(students[i])
    elif ch==3:
        print("프로그램이 종료되었습니다.")
        break
        