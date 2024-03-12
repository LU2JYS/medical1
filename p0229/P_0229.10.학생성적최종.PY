students = []
cnt = 0
while True: # 입력>출력>검색>삭제>수정
    print('-'*35)
    print('\t'+'[학생성적프로그램]')
    print('1. 학생성적입력') #####이름, 국, 영, 수 점수를 입력은 받으면 # [번호,이름,국,영,수,총합,평균,0]
    print('2. 학생성적수정') # 국, 영, 수 점수를 수정해 볼 수 있음. # (유의:국어를바꾸면, 합,평균)
    print('3. 학생성적삭제') # 도전!!
    print('4. 학생성적전체출력')  ####### 전체 출력 !!!!!!
    print('5. 학생검색출력') # 도전!!
    print('6. 등수처리')   # 얘빼고 다 할 수 는 있음.        
    print('0. 프로그램종료')  ####### 종료 !!!!
    print('-'*35)
    choice = input('원하는 번호를 입력하세요.>>')
    if choice.isdigit(): # 입력한게 숫자면 True
        choice = int(choice)
    if choice==1: # 1. 학생성적입력
        print('학생성적입력입니다.')
        cnt += 1
        stu_name = input('학생이름을 입력하세요.>>')
        kor = int(input('국어점수를 입력하세요.>>'))
        eng = int(input('영어점수를 입력하세요.>>'))
        math = int(input('수학점수를 입력하세요.>>'))
        total = kor+eng+math
        avg = total/3
        rank = 0
        student = [cnt,stu_name,kor,eng,math,total,avg,rank]
        students.append(student)
		#print(student)
    elif choice == 2: # 2. 학생성적수정
        modiName =  input('수정하고싶은 학생의 이름을 입력하세요 >> ')  
        for i, stu in enumerate(students): # [[1,'홍길동',100], [2,'이순신',90] ]
            # print(stu)
            if modiName in stu: # 학생이 검색이 될때
                print('{} 학생이 검색되었습니다.'.format(modiName))
                print('1.국어점수 수정')
                print('2.영어점수 수정')
                print('3.수학점수 수정')
                searchNo = input('수정할 과목 번호를 입력하세요.>>')
                if searchNo == '1':
                    print(' [  국어성적 수정  ] ' )
                    print('{}님의 현재 국어점수는 {}점입니다.'.format(stu[1],stu[2]))
                    ks = int(input('변경할 점수를 입력해주세요 >> '))
                    students[i][2] = ks # 국어점수 수정
                    # 총점수정 : 입력된 국어점수 + 기존의 영어점수+기존의 수학점수
                    students[i][5] = ks+students[i][3]+students[i][4]
                    # 평균수정 : 바뀐 총점을 활용해서 나누기 3 
                    students[i][6] = students[i][5]/3
                    print('국어점수가 변경되었습니다.!!')
                elif searchNo == '2':
                    print(' [  영어성적 수정  ] ' )
                    print('{}님의 현재 영어점수는 {}점입니다.'.format(stu[1],stu[3]))
                    es = int(input('변경할 점수를 입력해주세요 >> '))
                    students[i][3] = es # 영어점수 수정
                    students[i][5] = students[i][2]+es+students[i][4]
                    students[i][6] = students[i][5]/3
                    print('영어점수가 변경되었습니다.!!')

                elif searchNo == '3':
                    print(' [  수학성적 수정  ] ' )
                    print('{}님의 현재 수학점수는 {}점입니다.'.format(stu[1],stu[4]))
                    ms = int(input('변경할 점수를 입력해주세요 >> '))
                    students[i][4] = ms # 수학점수 수정
                    students[i][5] = students[i][2]+students[i][3]+ms
                    students[i][6] = students[i][5]/3
                    print('수학점수가 변경되었습니다.!!')
        

    elif choice == 3: # 3. 학생성적삭제
        delName = input('삭제하고싶은 학생의 이름을 입력하세요 >> ')        
        dchk = 0 # dchk=0일때는 학생이 존재하지 않음. dchk=1일때는 학생이 존재
        for i, stu in enumerate(students): # [[1,'홍길동',100], [2,'이순신',90] ]
            # print(stu)
            if delName in stu:
                del(students[i])
                print('삭제되었습니다.')
                dchk = 1
        if dchk == 0:
            print('입력하신 이름은 존재하지 않습니다.') 
    elif choice == 4: # 4. 학생성적전체출력
        print('[ 전체 학생 성적 ]')
        print('-'*60)
        print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
        print('-'*60)
        for s in range(len(students)): # len(student) = 학생의수
            print('{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}'.format(
            students[s][0],students[s][1],students[s][2],
            students[s][3],students[s][4],students[s][5],
            students[s][6],students[s][7])) # 홍길동
    elif choice == 5 : # 5. 학생검색출력'
        searchName = input('검색할 학생의 이름을 입력해주세요 >> ')
        chk = 0 # chk=0일때는 학생이 존재하지 않음. chk=1일때는 학생이 존재
        for stu in students: # [[1,'홍길동',100], [2,'이순신',90] ]
            # print(stu)
            if searchName in stu:
                #  print('{} 학생이 존재합니다.'.format(searchName))
                print('-'*60)
                print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
                print('-'*60)
                print('{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}'.format(
                    stu[0],stu[1],stu[2],stu[3],stu[4],stu[5],stu[6],stu[7]
                ))
                chk = 1
        if chk == 0:
            print('검색하신 학생이 존재하지 않습니다.')  
    elif choice == 6: # 6.등수처리
        print('등수처리')
        
        
        
    elif choice == 0:
        print('프로그램이 종료되었습니다.')
        break