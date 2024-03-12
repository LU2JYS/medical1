students=[]
student=[]
cnt=0
while True:
    print("-"*35)
    print("\t[학생성적프로그램]")
    print("-"*35)
    print("1. 학생성적입력") # 이름 국 영 수 총합 평균,0
    print("2. 학생성적수정")
    print("3. 학생검색")
    print("4. 학생 수정")#
    print("5. 등수처리")
    print("6. 학생정렬")
    print("0. 프로그램종료")#
    print("-"*35)
    ch= int(input("원하는 번호를 입력하시요"))
    
    if ch==1:
        #무한반복이되고있다.
        while True:
            cnt+=1
            print("학생성적을 입력하세요")
            print("-"*35)
            
            student= []
            name=input("이름를 입력하세요>>>>(-1.취소)")
            if name=="-1":
                    break
            student.append(cnt)
            student.append(name)
            student.append(int(input("국어 점수를 입력하세요>>>>")))
            student.append(int(input("영어 점수를 입력하세요>>>>")))
            student.append(int(input("수학 점수를 입력하세요>>>>")))
            sum = student[1]+student[2]+student[3] 
            avg=sum/3
                    #합계를 저장
            student.append(sum)
            student.append("{:.2f}".format(sum/3))
            students.append(student)
                    #전체학생 출력
            print("[학생성적 출력]")
            print("-"*50)
            print("학번\t이름\t국어\t영어\t수학\t합계\t평균")
            print("-"*50)
                
            for stu in students:
                for s in stu:   
                    print(s,end="\t")
                print() 
            print()
            print("-"*50)
                #2차원 리스트는 for문 2번을 사용함
                # 3명의 국어점수 합계,평균을 출력하시요
            avgs=0 
            kor=0
            for i,stu in enumerate(students):
                    kor=kor+stu[i][1]
                    print(kor)
                    
                # 3명의 수학점수 합계,평균을 출력하시요    
            math=0
            for i,stu in enumerate(students):
                    math=math+stu[3]
                    print(math)
                    
            eng=0
            for i,stu in enumerate(students):
                    eng=eng+stu[2]
                    print(eng)
                    
            totals +=stu[4]
            avg = totals/len(students)    
            print(kor,eng,math,totals,avg)
                
            avgs=totals/len(students)
            print("\t")
            print(kor,eng,math,totals,avg,sep="\t")
                
            
        
            
            #2.
    
    elif ch==4:
        print("입력하신 번호는 {}입니다.".format(ch))
        print(student)
        print("번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수")
        for s in range(len(student)):
            print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
            student[s][0],student[s][1],student[s][2],
            student[s][3],student[s][4],student[s][5],
            student[s][6],student[s][7],))
    
    elif ch==5:
        searchName=input("원하는 학생을 입력해 주세요>>>")
        for s, stu in enumerate(student):
            if searchName in stu:
                print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
            student[s][0],student[s][1],student[s][2],
            student[s][3],student[s][4],student[s][5],
            student[s][6],student[s][7],))
