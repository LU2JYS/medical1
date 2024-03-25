students=[[1,"홍길동",90,100,99,299,99.97],
        [2,"유관순",80,100,99,299,99.97],
        [3,"이순신",100,100,99,299,99.97]]

#찾는 학생의 입력을 받고

#찾고자하는 학생찾기
while True:
    search=input("검색하고 싶은 학생의 이름을 입력하세요>>>")
    chk=0 # 정보확인용
    if search =="0":
        break
    for stu in students:
        if stu[1]==search:
            print("{}의 학생 정보를 찾았습니다.".format(search))
    else:
        print("찾는 학생정보가 없습니다.")                
                
                
        