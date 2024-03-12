#for
student = [] 
for i in range(3): # 학생성적프로그램 반복 
    print('-'*35)
    print('\t[학생성적프로그램]')
    print('1.학생성적입력')# if 문을 사용해서 1누르면 [학생성적입력]
    print('4.학생성적전체출력')# 4 누르면 [학생성적전체출력]
    print('0.프로그램 종료')# 0 누르면 [프로그램 종료]
    print('-'*35)
    ch = input('원하는 번호를 입력하세요 >> ')
    if ch == '1' :
        print('학생성적입력')
        name = input('이름을 입력하세요 >> ')
        kor = int(input('국어점수를 입력하세요'))
        eng = int(input('영어점수를 입력하세요'))
        math = int(input('수학점수를 입력하세요'))
        # 한명의 학생의 정보를 담은 리스트
        s = [1,name,kor,eng,math,(kor+eng+math),(kor+eng+math)/3,0]
        student.append(s)
        #[[1,홍길동,100,100,100,300,100,0],[1,이순신,90,90..]]
        # print(student)
    elif ch == '4': # 전체학생리스트를 사용해서 출력
        print('학생성적출력')
        # 출력 for를 사용해서 학생 수 만큼 출력
        print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
        for s in range(len(student)): # len(student) = 학생의수
            print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
            student[s][0],student[s][1],student[s][2],
            student[s][3],student[s][4],student[s][5],
            student[s][6],student[s][7])) # 홍길동
   
    elif ch == '0':
        print('프로그램 종료')
    else: 
        print('잘못입력하셧습니다.')
    
    print('*'*35)

print('프로그램이 종료되었습니다. ')

    
        
    