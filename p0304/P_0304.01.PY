'''
변수종류 4가지에 꼭 기억하자
데이터베이스 프로그램



'''
student=[] #학생성적 저장할때
cnt=0 #학번사용
while True:
    print("-"*35)
    print("[학생성적프로그램]")
    print("-"*45)
    print("1. 학생성적입력")
    print("2. 학생성적 전체출력")
    print("3. 학생성적")
    print("4. 등수처리")
    print("0. 프로그램 종료")
    print("-"*45)
    choice= input("원하는 번호를 입력하세요")
    if not choice. isdigit():
        print('숫자만 입력가능합니다')
        continue #반복문 다시 실행:
    choice=int(choice)
    
    #1번 학생성적입력 프로그램
    if choice== 1:
        print("학생성적을 입력하세요")
    
    #2. 학생성적수정 프로그램
    elif choice==2:
        
    
    #0. 프로그램 종료
    elif choice ==0:
        print("프로그램을 종료합니다")
        break # 반복문 종료
        