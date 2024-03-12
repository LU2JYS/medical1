students=[[1,"홍길동",90,100,99,299,99.97],
        [2,"유관순",80,100,99,299,99.97],
        [3,"이순신",100,100,99,299,99.97]]

#찾는 학생의 입력을 받고

#찾고자하는 학생찾기
while True:
    
    search=input("검색하고 싶은 학생의 이름을 입력하세요>>>")
    chk=0 # 찾는 정보확인용
    count=0
    if search =="0":
        break
    for stu in students: #먼저 홍길동,유관순,이순신 순으로 빼온다.
            if search in stu:
                chk=1 #정보를 찾으면 정보를 1로 변경
                break  #일치하면 브레이크로 나오게된다.
            count+=1
            
    if (chk==1):
        print("[{} 학생정보 출력]".format(search))
        print('-'*35)
        print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
        print('-'*35)
        for i in students[count]:
            print(i,end="\t")
        print()         
    else:
        print("찾는 학생정보가 없습니다.")   
        
                
                
        